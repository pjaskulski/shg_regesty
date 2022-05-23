""" tworzenie list regestów ze Słownika Historyczno-Geograficznego """

import re
import csv
import sys
from pathlib import Path
import openpyxl
from tools import create_sheet, get_regesty, get_year_from_regest
from tools import get_source_from_regest, get_contents_from_regest


# mamy bardzo duże pola i bez zwiększenia limitu skrypt się wykłada
csv.field_size_limit(sys.maxsize)

slowniki = {1: 'Benedyktyni',
            2: 'Chełmno',
            3: 'Kraków',
            4: 'Lublin',
            5: 'Lublin_zaginione',
            6: 'Płock',
            7: 'Poznań',
            8: 'Sanok',
            9: 'Wieluń',
            10: 'Wyszogród',
            11: 'Warszawa',
            12: 'Liw'
}

lista = {
            r'włas[n]?\.\s+szlach\.':'szlachecka',
            r'włas[n]?\.\s+kl\.':'klasztorna',
            r'włas[n]?\.\s+opata':'opata',
            r'włas[n]?\.\s+konw.':'konwentu',
            r'włas[n]?\.\s+ryc\.':'rycerska',
            r'należy\s+do\s+stołu\s+konw\.':'konwentu',
            r'należy\s+do\s+bpa\s+lubus\.':'biskupia',
            r'własn\.\s+podzielona\.':'podzielona',
            r'wieś\s+szlach\.':'szlachecka',
            r'należy\s+do\s+kl\.':'klasztorna',
            r'włas[n]?\.\s+wwdy':'wojewody',
            r'należy\s+do\s+[a-zA-ząśężźćńłó]+\s+stołu\s+opata':'opata',
            r'należy\s+do\s+stołu\s+opata':'opata',
            r'włas[n]?\.\s+rządu':'rządowa',
            r'włas[n]?\.\s+król\.':'królewska',
            r'należy\s+do\s+króla':'królewska',
            r'należy\s+do\s+opactwa':'opata',
            r'włas[n]?\.\s+szlach\.\s+i\s+prep\.':'szlachecka, prepozyta',
            r'włas[n]?\.\s+bpa':'biskupia',
            r'włas[n]?\.\s+szlach\.,\s+następnie\s+kl\.':'szlachecka, klasztorna',
            r'włas[n]?\.\s+bpa[a-zA-Z\.\s]+,\s+następnie\s+rządowa':'biskupia, rządowa',
            r'włas[n]?. kl.[a-zA-Ząśężźźćńłó\.,\s]+pleb\.,\s+[a-zA-Zśężźćńłó]\s+szlach\.':'klasztorna, plebana, szlachecka',
            r'włas[n]?\.\s+kl\.[a-zA-Ząśężźźćńłó\.,\s]+prep\.':'klasztorna, prepozyta',
            r'włas[n]?\.\s+bp':'biskupia',
            r'włas[n]?\.\s+arcbpstwa':'arcybiskupia',
            r'włas[n]?\.\s+książęca':'książęca',
            r'włas[n]?\.\s+książęca[a-zA-Z1-9ąśężźźćńłó\.,\s]+\s+król\.':'książęca, królewska',
            r'włas[n]?\.\s+książęca[a-zA-Ząśężźćńłó,\s]+szlach\./gm':'książęca, szlachecka',
            r'włas[n]?\.\s+książąt':'książęca',
            r'włas[n]?\.\s+książęca[a-zA-Ząśężźćńłó,\s]+kl\.':'książęca, klasztorna'
        }


def remove_html(value: str) -> str:
    # czyszczenie z pozostałości HTML-a
    pattern = r'<.*?>'
    value = re.sub(pattern, '', value)
    value = value.replace(r'\n', ' ')
    return value


def process_point(sheet, m_id, m_nazwa, point_num, point_text):
    """przetwarzanie treści punktu z zapisem do wskazanego arkusza
       sheet - wskazanie na arkusz
       m_id - identyfikator miejscowości
       nazwa - nazwa miejscowości
       point_num - numer punktu
       point_text - treść punktu
    """
    global regesty_count
    global place_owner

    reg_list = []
    point = point_num

    # if 'Własn. szlach. w kluczu melsztyńskim' in point_text:
    #     print()

    reg_list, ownership = get_regesty(point_text)

    reg_list = [remove_html(reg) for reg in reg_list]

    if reg_list:
        # pierwszy regest może wymagać podzielenia
        pattern = r'\.\s{1}\d{4}'
        pattern2 = r'\s+r\.\s{1}\d{4}'
        match = re.search(pattern, reg_list[0])
        match2 = re.search(pattern2, reg_list[0])
        if match and not match2:
            pos = reg_list[0].find('. 1')
            if pos != -1:
                part1 = reg_list[0][:pos + 1]
                part2 = reg_list[0][pos + 2:]
                reg_list[0] = part2
                reg_list.insert(0, part1)

    # własność
    if point_num == 3:
        for reg in reg_list:
            year = get_year_from_regest(reg)
            for pattern, owner_type in lista.items():
                match = re.search(pattern, reg.lower())
                if match:
                    if (m_id, year) in place_owner:
                        _m_id, _year, owner_types = place_owner[(m_id, year)]
                        if owner_type not in owner_types:
                            if not owner_types.endswith(','):
                                owner_types += ', '
                            owner_types += owner_type
                            place_owner[(m_id, year)] = (m_nazwa, year, owner_types)
                    else:
                        place_owner[(m_id, year)] = (m_nazwa, year, owner_type)

    # specjalna obsługa dla p. 1
    if point_num == 1:
        new_reg_list = []
        for item in reg_list:
            if ")," in item:
                tmp = item.split("),")
                tmp = [r+')' if not r.endswith(")") else r for r in tmp]
                new_reg_list = new_reg_list + tmp
            elif ")." in item:
                tmp = item.split(").")
                tmp = [r+')' if not r.endswith(")") else r for r in tmp]
                new_reg_list = new_reg_list + tmp
            else:
                new_reg_list.append(item)
        reg_list = new_reg_list

    prev_year = ''
    regest_num = 0
    for item in reg_list:
        # if 'n. par. Nowa Słupia (DLb. II 490) [' in item:
        #     print()
        item = item.strip()
        year = get_year_from_regest(item)
        # jeżeli regest nie ma roku to przyjmujemy poprzedni
        if year.strip() == '' and regest_num > 0 and prev_year != '':
            year = prev_year + '!'
        else:
            prev_year = year
        source = get_source_from_regest(item)
        contents = get_contents_from_regest(item, year, source, m_nazwa)
        contents = contents.replace('[@', '[').replace('@]',']')
        item = item.replace('[@', '[').replace('@]',']')
        tmp_regest = [m_id, m_nazwa, point, year, contents, source, item]
        regest = tuple(tmp_regest)
        sheet.append(regest)
        regesty_count[point_num] += 1
        regest_num += 1
        


# -------------- Główny program ------------------------------------------------
if __name__ == '__main__':
    regesty_count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

    for nr in range(1, 13):
        print(f"Słownik: {slowniki[nr]} ({nr})")

        place_owner = {}

        output_path = Path('.').parent / f'output/regesty_{slowniki[nr]}.xlsx'
        input_path = Path('.').parent / f'output/hasla_{nr}_pkt.csv'

        wb = openpyxl.Workbook()
        ws = wb.active

        point_sheet_columns = ['Miejscowość_Id', 'Nazwa', 'Punkt', 'Rok',
                               'Treść', 'Źródła', 'Cały Regest']
        regest_sheet_1 = create_sheet(wb=wb, title="Regesty p. 1", columns=point_sheet_columns)
        regest_sheet_2 = create_sheet(wb=wb, title="Regesty p. 2", columns=point_sheet_columns)
        regest_sheet_3 = create_sheet(wb=wb, title="Regesty p. 3", columns=point_sheet_columns)
        regest_sheet_4 = create_sheet(wb=wb, title="Regesty p. 4", columns=point_sheet_columns)
        regest_sheet_5 = create_sheet(wb=wb, title="Regesty p. 5", columns=point_sheet_columns)
        regest_sheet_6 = create_sheet(wb=wb, title="Regesty p. 6", columns=point_sheet_columns)

        # przetwarzanie wierszy
        with open(input_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter='#')
            #lines = len(list(csv_reader))
            licznik = 0
            for row in csv_reader:
                licznik += 1
                print(f'Przetwarzam wiersz {licznik}.')
                miejsce_id = row['id'].strip()
                nazwa = row["header"]
                nazwa = re.sub(r'<.*?>', '', nazwa)
                p0 = row['0'].strip()
                p1 = row['1'].strip()
                p2 = row['2'].strip()
                p3 = row['3'].strip()
                p4 = row['4'].strip()
                p5 = row['5'].strip()
                p6 = row['6'].strip()
                p7 = row['7'].strip()
                p8 = row['8'].strip()
                p9 = row['9'].strip()

                # Punkt 1
                if p1:
                    process_point(regest_sheet_1, miejsce_id, nazwa, 1, p1)
                if p2:
                    process_point(regest_sheet_2, miejsce_id, nazwa, 2, p2)
                if p3:
                    process_point(regest_sheet_3, miejsce_id, nazwa, 3, p3)
                if p4:
                    process_point(regest_sheet_4, miejsce_id, nazwa, 4, p4)
                if p5:
                    process_point(regest_sheet_5, miejsce_id, nazwa, 5, p5)
                if p6:
                    process_point(regest_sheet_6, miejsce_id, nazwa, 6, p6)

        # usunięcie pustego pierwszego arkusza
        sheet1 = wb['Sheet']
        wb.remove(sheet1)

        # arkusz z własnością
        wlasnosc_sheet = create_sheet(wb=wb, title="Własność", columns=['Miejsc_ID', 'Miejscowość', 'Rok', 'Własność'])
        for key_tuple, owner_lista in place_owner.items():
            miejscowosc_id, _year = key_tuple
            miejscowosc, rok, owner_types = owner_lista

            # bez powtórzeń typów własności
            tmp = owner_types.split(',')
            if len(tmp) > 1:
                tmp = [t.strip() for t in tmp]
                tmp = list(set(tmp))
                owner_types = ', '.join(tmp)

            wiersz = (miejscowosc_id, miejscowosc, rok, owner_types)
            wlasnosc_sheet.append(wiersz)

        # zapis pliku xlsx
        wb.save(filename=output_path)

    suma = 0
    for i in range(1, 7):
        print(f"p.{i}", regesty_count[i])
        suma += regesty_count[i]
    print(f"razem: {suma}")
