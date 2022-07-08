""" Analiza występowania i tagowania urzędów i funkcji - dane z csv """

import re
import os
import csv
import sys
from pathlib import Path
import spacy
from spacy.matcher import Matcher
from soltysi import rule_patterns

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

def clear_text(text: str) -> str:
    """ czyści tekst z tagów html, odnośników bibliograficznych"""
    # nawiasy
    pattern = r'[\(\[].*?[\)\]]'
    text = re.sub(pattern, '', text)
    pattern = r'<.*?>'
    text = re.sub(pattern, '', text)
    text = text.replace(r'\n', ' ')

    return text


if __name__ == "__main__":
    nlp = spacy.load("pl_core_news_lg")
    
    for nr in range(1, 13):
        print(f"Słownik: {slowniki[nr]} ({nr})")
        matcher = Matcher(nlp.vocab)
        patterns = rule_patterns(slowniki[nr])
        matcher.add("Soltysi", patterns=patterns)

        lista = []

        input_path = Path('.').parent / f'output/data{nr}hasla.csv'
        output_path = Path('.').parent / f'output/soltysi_{slowniki[nr]}.txt'
        text_path = Path('.').parent / f'output/soltysi_text_{slowniki[nr]}.txt'

        if os.path.exists(text_path):
            os.remove(text_path)

        with open(input_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                header = row["header"]
                header = clear_text(header)
                print(header)

                body = row["body"]
                if body:
                    p_full = clear_text(body)

                # z zapisem analizowanej treści do dodatkowego pliku
                #with open(text_path, "a", encoding='utf-8') as f_text:
                #for point in p_full:
                #    if p_full:
                #        f_text.write(f'{p_full}\n\n')

                    doc = nlp(p_full)
                    matches = matcher(doc)

                    # tylko nie zawierające się znaleziska
                    spans = [doc[start:end] for _, start, end in matches]
                    for span in spacy.util.filter_spans(spans):
                        funkcja = span.text
                        funkcja = re.sub(r'\d', '', funkcja)
                        funkcja = funkcja.replace('/','').replace('½', '').replace(';','').strip()
                        funkcja = funkcja.replace('–','').replace(':', '')
                        pattern = r'[A-ZŚŻŹĆŁ]{1}\.$'
                        match = re.search(pattern, funkcja)
                        if match:
                            skrot_miejsc = match.group()[0]
                            if header.startswith(skrot_miejsc):
                                funkcja += f' ({header})'
                        lista.append(funkcja)

        # zapis pliku z wynikami dla danego słownika
        with open(output_path, "w", encoding='utf-8') as f:
            lista = list(set(lista))
            for item in sorted(lista, key=str.casefold):
                f.write(f'{item}\n')
