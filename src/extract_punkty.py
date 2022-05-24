# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 07:24:49 2021

INPUT: input    
    csv zawierający hasła słownikowe (browsingGroup oznaczone literami) z wybranego słownika

OUTPUT: "hasla_id_name.csv", "hasla_id_name.xlsx", "data_pkt.csv", "data_pkt.xlsx"
    csv (UWAGA: rozdzielany znakiem "#" - nie występuje w tresci haseł) i xlsx osobno: 
    hasla_id_name: zawiera nazwę, id, punkty od 0 do 9 (plus uwagi w 10)
    data_pkt: oryginalny zbiór danych (haseł słownikowych) z dołożonymi kolumnami 0 do 10 (j.w.)

@author: Anna Fiedukowicz https://github.com/fragaria1/SHG_feature_extraction
(modyfikacje: Piotr Jaskulski)
"""

import pandas as pd
import re
from pathlib import Path


def clear_html(text:str) -> str:
    pattern = r'<.*?>'
    text = re.sub(pattern, '', text)
    text = text.replace(r'\n', '')
    return text.strip()


def remove_span_from_broken_html(text:str) -> str:
    start = '<span class="pageNumber"'
    stop = '</span>'

    find_tag = True
    while find_tag:
        pos1 = text.find(start)
        if pos1 == -1:
            find_tag = False
        else:
            pos2 = text.find(stop, pos1)
            if pos2 == -1:
                find_tag = False
            else:
                text = text[:pos1] + text[pos2+len(stop):]

    return text


def ext_punkty(output_path, hasla_path):
    ############################### DANE ##########################################
    data = pd.read_csv(hasla_path, sep=",")
    #sprawdzenie wczytanych nazw kolumn
    data.columns

    body = data.iloc[:,10]

    ######################## wydzielenie uwag, wstępu i punktów  ##########################
    listoflists = [None]*len(body)

    for j, item in enumerate(body):
        temp = [None]*11
        temporal = item

        # usuwam page number
        if type(temporal) == type(''):
            temporal = remove_span_from_broken_html(temporal)
        else:
            listoflists[j] = list()
            continue

        # if '1206 Cirnicov, 1208 Chirnicov, 1212 Cyrnichou' in temporal:
        #     print()

        test_start = "</p>\\\\n<p><b>[1-8]{1}[ABCDEFabcdef]{0,1}\.[234]{0,1}\.?</b>"
        test_start1 = '</p>\\\\n<p><b>Uw\.</b>'
        test_start2 = '</p>\\\\n<p><b>Uwaga:</b>'
        test_start3 = '</p>\\\\n<p><b>-[abcde]{0,1}\.</b>'
        test_start4 = '<b>-[a]{0,1}\.</b>'

        if re.search(test_start, temporal):
            pattern = test_start + '|' + test_start1 + '|' + test_start2 + '|' + test_start3 + '|' + test_start4
            parts = re.split(pattern, temporal)
            punkty = [clear_html(point_symbol.group()) for point_symbol in re.finditer('(' + pattern + ')', temporal)]
            licznik = 0
            p_value = {}

            p_value['0'] = parts[0]

            for p in punkty:
                licznik += 1
                p_value[p] = parts[licznik]

            prev_nr = 0
            for key, value in p_value.items():
                if key[0].isnumeric():
                    nr = int(key[0])
                    if len(key) > 1 and key[1] != '.':
                        value = '{' + key + '}' + value
                elif key[0].lower() == 'u':
                    nr = 9
                elif key in ['-a.', '-b.', '-c.', '-d.', '-e.', '-f.']:
                    nr = prev_nr
                    value = '{' + key + '}' + value

                prev_nr = nr

                if temp[nr]:
                    temp[nr] = temp[nr] + ';' + value
                else:
                    temp[nr] = value
        else:
            temp[0] = temporal

        listoflists[j]=temp

    hasla_df = pd.DataFrame(listoflists)
    data_pkt = pd.concat([data, hasla_df], axis=1)
    #data_pkt.to_excel(Path(output_path,f"hasla_{nr_slownika}_pkt.xlsx"))
    data_pkt.to_csv(output_path, sep="#", index_label="id")

