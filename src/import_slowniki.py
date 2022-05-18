""" Skrypt importujący słownik z pliku CSV """

from pathlib import Path
from extract_punkty import ext_punkty


if __name__ == '__main__':
    file_name = Path('.').parent / 'data/entries_202109141551.csv'
    # 1 - Benedyktyni
    # 2 - Chełmno
    # 3 - Kraków
    # 4 - Lublin
    # 5 - Lublin zaginione  
    # 6 - Płock
    # 7 - Poznań
    # 8 - Sanok
    # 9 - Wieluń
    # 10 - Wyszogród
    # 11 - Warszawa
    # 12 - Liw
    #dict_numb = 12
    output_path = Path('.').parent / 'output/wyniki/'
    #ext_slownik(file_name, dict_numb, output_path)

    for i in range(1, 13):
        ext_punkty(i, output_path)
