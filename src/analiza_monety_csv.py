""" Analiza występowania i tagowania jednostek monetarnych - dane z csv """

import re
import os
import csv
import sys
from pathlib import Path
import spacy
from spacy.matcher import Matcher
from monety import false_coins_list, rule_patterns

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
    patterns = rule_patterns()
    false_coins = false_coins_list()

    nlp = spacy.load("pl_core_news_lg")
    matcher = Matcher(nlp.vocab)
    matcher.add("Monety", patterns=patterns)

    for nr in range(1, 13):
        print(f"Słownik: {slowniki[nr]} ({nr})")
        lista = []

        input_path = Path('.').parent / f'output/data{nr}hasla.csv'
        output_path = Path('.').parent / f'output/monety_{slowniki[nr]}.txt'
        text_path = Path('.').parent / f'output/text_{slowniki[nr]}.txt'

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
                with open(text_path, "a", encoding='utf-8') as f_text:
                #for point in p_full:
                    if p_full:
                        f_text.write(f'{p_full}\n\n')

                        doc = nlp(p_full)
                        matches = matcher(doc)

                        # tylko nie zawierające się znaleziska
                        spans = [doc[start:end] for _, start, end in matches]
                        for span in spacy.util.filter_spans(spans):
                            moneta = span.text
                            moneta = re.sub(r'\d', '', moneta)
                            moneta = moneta.replace('/','').replace('½', '').replace(';','').strip()
                            moneta = moneta.replace('–','').replace(':', '')
                            if moneta not in false_coins:
                                lista.append(moneta)

        # zapis pliku z wynikami dla danego słownika
        with open(output_path, "w", encoding='utf-8') as f:
            lista = list(set(lista))
            for item in sorted(lista, key=str.casefold):
                f.write(f'{item}\n')
