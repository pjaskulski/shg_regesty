""" definicja reguł dla wyszukiwania urzedów w SHG """


def rule_patterns(slownik:str ='') -> list:
    """ definicje reguł """
    patterns = [
        # wójt + przymiotnik (lub parę przymiotników)
        [{"LEMMA":"wójt"}, {"POS":"ADJ", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"POS":"ADJ", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"POS":"ADJ", "OP": "+"}],
        # wójt + przymiotnik i przymiotnik
        [{"LEMMA":"wójt"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LEMMA":"wójtowy"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LEMMA":"wójcina"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        # wójt + nazwa własna (lub parę nazw)
        [{"LEMMA":"wójt"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"POS":"PROPN", "OP": "+"}],
        # wójt + przymiotnik + nazwa własna (lub parę nazw)
        [{"LEMMA":"wójt"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        # wójt + rzeczownik
        [{"LEMMA":"wójt"}, {"POS":"NOUN"}],
        [{"LEMMA":"wójtowy"}, {"POS":"NOUN"}],
        [{"LEMMA":"wójcina"}, {"POS":"NOUN"}],
        # wójt w nazwa (lub parę)
        [{"LEMMA":"wójt"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        # wójt z nazwa
        [{"LEMMA":"wójt"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        # wójt m. nazwa
        [{"LEMMA":"wójt"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        # wójt wsi nazwa
        [{"LEMMA":"wójt"}, {"LOWER":"wsi"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"LOWER":"wsi"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"LOWER":"wsi"}, {"POS":"PROPN", "OP": "+"}],
        # wójt z wsi nazwa
        [{"LEMMA":"wójt"}, {"LOWER":"z"}, {"LOWER":"wsi"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"LOWER":"z"}, {"LOWER":"wsi"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"LOWER":"z"}, {"LOWER":"wsi"}, {"POS":"PROPN", "OP": "+"}],
        # wójt ze wsi nazwa
        [{"LEMMA":"wójt"}, {"LOWER":"ze"}, {"LOWER":"wsi"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójtowy"}, {"LOWER":"ze"}, {"LOWER":"wsi"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wójcina"}, {"LOWER":"ze"}, {"LOWER":"wsi"}, {"POS":"PROPN", "OP": "+"}],
        # wójt sądu najwyższego pr. niem. na zamku krak.
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"na"}, {"LEMMA":"zamek"}, {"LOWER":"krak"}, {"IS_PUNCT":True}],
        # wójt sądu pr. niem. w kluczu łąckim
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"LEMMA":"klucz"}, {"POS":"ADJ"}],
        # wójt sądu wyższego dworskiego kl. miech.
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ", "OP":"+"}, {"LOWER":"kl"}, {"IS_PUNCT":True}, {"LOWER":"miech"}, {"IS_PUNCT":True}],
        # wójt sądu najw. pr. niem. na zamku krak.
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"LOWER":"najw"}, {"IS_PUNCT":True}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"na"}, {"LEMMA":"zamek"}, {"LOWER":"krak"}, {"IS_PUNCT":True}],
        # wójt sądu wyższego pr. niem. w + nazwa (klasztor, zamek, miasto)
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"POS":"NOUN", "OP":"+"}],
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"POS":"PROPN", "OP":"+"}],
        # wójt sądu leńskiego w + nazwa
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"w"}, {"POS":"PROPN", "OP":"+"}],
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"w"}, {"POS":"NOUN", "OP":"+"}],
        # wójt sądu wyższego dworskiego pr. niem. + nazwa
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP":"+"}],
        # wójt sądu wyższego pr. niem. magd.
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"LEMMA":"prawo"}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"magd"}, {"IS_PUNCT":True}],
        # wójt sądu prawa niem.
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"LEMMA":"prawo"}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        # wójt sądu wyższego prawa niem.
        [{"LEMMA":"wójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LEMMA":"prawo"}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        # wójt i mieszcz. z nazwa, wójt i mieszczanin z nazwa, wójt i mieszcz. nazwa
        [{"LEMMA":"wójt"}, {"LOWER":"i"}, {"LEMMA":"mieszcz"}, {"IS_PUNCT":True}, {"LOWER":"z"}, {"POS":"PROPN"}],
        [{"LEMMA":"wójt"}, {"LOWER":"i"}, {"LEMMA":"mieszczanin"}, {"LOWER":"z"}, {"POS":"PROPN"}],
        [{"LEMMA":"wójt"}, {"LOWER":"i"}, {"LEMMA":"mieszcz"}, {"IS_PUNCT":True}, {"POS":"PROPN"}],
        [{"LEMMA":"wójt"}, {"LOWER":"i"}, {"LEMMA":"mieszczanin"}, {"POS":"PROPN"}],
    ]

    if slownik == 'Benedyktyni':
        shortcuts = ["gnieźn", "kiel", "koz", "król", "lub", "lubus", "łysog", "opat", "pap", "rad",
                    "sand", "sieciech", "sier", "święt", "tyn", "urzęd", "wąch", "wąwol", "wiśl",
                    "włocł"]
    elif slownik == 'Chełmno':
        shortcuts = ["bierzg", "brat", "brod", "chełm", "dzierzg", "gol", "grudz", "kol",
                    "kow", "krzyż", "kuj", "kurz", "lip", "lub", "magd", "maz", "mich",
                    "miej", "płoc", "pokrz", "pomez", "radz", "rog", "starogr", "tor", "unisł",
                    "warm", "włocł"]
    elif slownik == 'Kraków':
        shortcuts = ["krak", "lel", "biec", "chęc", "czchow", "czech", "czes", "frank", "gnieźn",
                    "imbr", "jędrz", "kal", "Klar", "koprz", "ksiąs", "lub", "łęcz", "magd", "maz",
                    "miech", "miej", "mog", "mstow", "niem", "opocz", "ośw", "pilzn", "pol", "poł",
                    "pozn", "pras", "prosz", "przem", "rad", "roz", "san", "sand", "sądec",
                    "sieciech", "sier", "siew", "staniąt", "starosądec", "szczyrz", "śl", "średz",
                    "świętokrz", "świętop", "tyn", "wąch", "węg", "wiel", "wiśl", "wojn", "zator",
                    "zawich", "zwierzyn", "żarn", "żyd"]
    elif slownik == "Czersk":
        shortcuts = ["bełs", "bial", "biel", "bł", "brzeskuj", "chełm", "ciech", "czer", "czerw",
                    "droh", "garw", "gąb", "gnieźn", "gost", "grodz", "grój", "kal", "kam", "koln",
                    "krak", "krzyż", "lit", "liw", "lub", "łęcz", "łomż", "łuk", "magd", "mak",
                    "maz", "miej", "mław", "nowom", "ostroł", "ostrow", "płoc", "płoń", "pol",
                    "pozn", "przas", "pułt", "rac", "rad", "radz", "raw", "roż", "sand", "sąch",
                    "ser", "sierp", "soch", "stęż", "szreń", "tarcz", "war", "warsz", "wąs", "węg",
                    "wil", "wis", "wlkp", "włocł", "wysz", "zakr", "zawkrz", "ziem", "żyd."]
    elif slownik == 'Lublin':
        shortcuts = ["krak", "lub", "łuk", "magd", "rad", "sand", "węg"]
    elif slownik == 'Lublin_zaginione':
        shortcuts = [] # nie ma skrótów geograficznych?
    elif slownik == 'Płock':
        shortcuts = ["biel", "bł", "chełm", "ciech", "czer", "czerw", "dobrz", "flam", "gniezn",
                    "gost", "grodz", "grój", "kam", "kol", "krak", "krzyż", "kuj", "liw", "łęcz",
                    "łom", "łow", "magd", "mak", "maz", "miej", "mław", "niedzb", "now", "nowogr",
                    "ostroł", "ostrow", "płoc", "płoń", "pom", "pozn", "pras", "przas", "pułt",
                    "rac", "raw", "róż", "sąch", "ser", "siel", "sierp", "soch", "szr", "śląs",
                    "war", "warsz", "wąs", "węg", "wis", "wysz", "zakr", "zamb", "zawkrz", "żyd."]
    elif slownik == 'Poznań':
        shortcuts = ["bab", "biech", "bledz", "bnin", "brand", "buk", "bydg", "chełm", "czarnk",
                    "dobrz", "flam", "frank", "giec", "głog", "gnieźn", "inowrocł", "kal", "kam",
                    "karczm", "karz", "kcyn", "klar", "kon", "kostrz", "kośc", "krak", "krob",
                    "krusz", "krzyw", "ksiąs", "kuj", "lądz", "lub", "łekn", "łęcz", "magd", "maz",
                    "miej", "międz", "młp", "mod", "mogil", "nak", "niem", "ober", "odol", "ołob",
                    "opat", "ostrz", "owin", "parad", "pobiedz", "pol", "pom", "pozn", "pras", "przem",
                    "pszcz", "pyzdr", "radz", "rogoz", "sant", "sier", "soł", "starogr", "śląs",
                    "średz", "śrem", "trzem", "wał", "wągr", "węg", "wielich", "wlkp", "włocł",
                    "wrocł", "wsch", "zbąsz", "żnin", "żon", "żyd."]
    elif slownik == 'Sanok':
        shortcuts = ["biec", "gr", "krak", "krośn", "lw", "łac", "magd", "niem", "pilzn", "pol",
                    "przem", "samb", "san", "sandom", "sądec", "węg", "żydacz."]
    elif slownik == 'Wieluń':
        shortcuts = ["bolesł", "gnieźń", "kal", "krak", "magd", "miej", "niem", "ostrz", "pozn",
                    "sier", "średz", "wiel", "wrocł."]
    elif slownik == 'Wyszogród':
        shortcuts = ["biel", "Bł", "chełm", "Ciech", "czer", "Czerw", "dobrz", "gniezn", "Gost",
                    "grój", "Kam", "kol", "liw", "Łęcz", "łom", "Łow", "mak", "Maz", "miej", "mław",
                    "Niedz", "nur", "Ostroł", "ostrow", "płoc", "płoń", "pozn", "pras", "Przas",
                    "Pułt", "Rac", "raw", "róż", "Ser", "siel", "Soch", "Szr", "war", "Warsz",
                    "Wąs", "węg", "wis", "Wysz", "Zakr", "Zamb", "zawkrz."]
    elif slownik == 'Warszawa':
        shortcuts = ["bełs", "bł", "chełm", "ciech", "czer", "czerw", "gnieźn", "gost", "grój",
                    "kam", "krak", "krzyż", "liw", "łęcz", "łomż", "magd", "mak", "maz", "miej",
                    "nur", "ostroł", "ostrow", "płoc", "płoń", "pol", "pozn", "pras", "pułt",
                    "rac", "raw", "roż", "sand", "ser", "soch", "tarcz", "war", "warsz", "węg",
                    "wis", "wlkp", "włocł", "wysz", "zakr", "zawkrz", "żyd."]
    elif slownik == 'Liw':
        shortcuts = ["bełs", "bial", "biel", "bł", "chełm", "ciech", "czer", "czerw", "droh",
                    "garw", "gąb", "gnieźn", "gost", "grodz", "grój", "kam", "koln", "krak",
                    "król", "krzyż", "lit", "liw", "łęcz", "łomż", "łuk", "magd", "mak", "maz",
                    "miej", "mław", "mszczon", "niedz", "niem", "nowom", "nur", "ostroł", "ostrow",
                    "płoc", "płoń", "pol", "pozn", "pras", "przas", "pułt", "rac", "radz", "raw",
                    "roż", "sand", "sąch", "ser", "sierp", "soch", "szreń", "tarcz", "war", "warsz",
                    "wąs", "węg", "wil", "wis", "wlkp", "włocł", "wysz", "zakr", "zamb", "zawkrz",
                    "ziem", "żyd."]
    litery = 'ABCDEFGHIJKLMNOPRSTUWZŚŻŹĆŁ'
    for shortcut in shortcuts:
        # wójt + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"wójt"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójtowy"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójcina"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # wójt + 'z' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"wójt"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójtowy"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójcina"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # wójt + 'w' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"wójt"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójtowy"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójcina"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])

        # wójt + 'm' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"wójt"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójtowy"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wójcina"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])

        # wójt z + skrót miejscowości np.: A.
        for litera in litery:
            patterns.append([{"LEMMA":"wójt"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"wójtowy"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"wójcina"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])

    return patterns
