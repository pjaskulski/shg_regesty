""" definicja reguł dla wyszukiwania urzedów w SHG """


def rule_patterns(slownik:str ='') -> list:
    """ definicje reguł """
    patterns = [
        # sędzia + przymiotnik (lub parę przymiotników)
        [{"LEMMA":"sędzia"}, {"POS":"ADJ", "OP":"+"}],
        # sędzia + przymiotnik i przymiotnik
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        # sędzia + nazwa własna (lub parę nazw)
        [{"LEMMA":"sędzia"}, {"POS":"PROPN", "OP": "+"}],
        # sędzia + przymiotnik + nazwa własna (lub parę nazw)
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        # sędzia + rzeczownik (lub parę)
        [{"LEMMA":"sędzia"}, {"POS":"NOUN", "OP":"+"}],
        # sędzia w nazwa (lub parę nazw)
        [{"LEMMA":"sędzia"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        # sędzia z nazwa (lub parę nazw)
        [{"LEMMA":"sędzia"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        # sędzia m. nazwa
        [{"LEMMA":"sędzia"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        # sędzia miasta nazwa
        [{"LEMMA":"sędzia"}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        # sędzia w mieście nazwa
        [{"LEMMA":"sędzia"}, {"LOWER":"w"}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        # sędzia wsi nazwa
        [{"LEMMA":"sędzia"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        # sędzia z wsi nazwa
        [{"LEMMA":"sędzia"}, {"LOWER":"z"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        # sędzia ze wsi nazwa
        [{"LEMMA":"sędzia"}, {"LOWER":"ze"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        # sędzia we wsi nazwa
        [{"LEMMA":"sędzia"}, {"LOWER":"we"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        # sędzia sądu wyższego pr. niem. na + nazwa
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"na"}, {"POS":"PROPN"}],
        # sędzia sądu leńskiego na + nazwa (lub w + nazwa)
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"na"}, {"POS":"PROPN"}],
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"LOWER":"na"}, {"POS":"PROPN"}],
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"LEMMA":"leński"}, {"LOWER":"na"}, {"POS":"PROPN"}],
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"w"}, {"POS":"PROPN"}],
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"LOWER":"w"}, {"POS":"PROPN"}],
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"LEMMA":"leński"}, {"LOWER":"w"}, {"POS":"PROPN"}],
        # sędzia sądu leńskiego + przymiotnik
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"POS":"ADJ"}],
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"LEMMA":"leński"}, {"POS":"ADJ"}],
        # sąd leński goleski (generalnie z 2 przymiotnikami)
        [{"LEMMA":"sąd"}, {"POS":"ADJ"}, {"POS":"ADJ"}],
        # sędzia sądu pr. niem. + nazwa
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"POS":"PROPN"}],
        # sędzia sądu wyższego dworskiego pr. niem.
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        # sędzia sądu wyższego dworskiego + nazwa
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"POS":"ADJ"}, {"POS":"PROPN"}],
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"POS":"PROPN"}],
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"LEMMA":"wysoki"}, {"LEMMA":"dworski"}, {"POS":"PROPN"}],
        # sędzia sądu wyższego dworskiego
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP":"?"}],
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP":"?"}],
        # sędzia sądu sołeckiego
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}],
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"LEMMA":"sołecki"}],
        [{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"LOWER":"sołeckiego"}],
        [{"LEMMA":"sędzia"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}],

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
        # sędzia + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"sędzia"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # sędzia + 'z' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"sędzia"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # sędzia + 'w' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"sędzia"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # sędzia + 'm' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"sędzia"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # sędzia sądu leńskiego na + rzeczownik + skrót (geograficzny)
        patterns.append([{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"na"}, {"POS":"NOUN"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # sędzia sądu + przymiotnik + skrót geogr.
        patterns.append([{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        
        # sędzia z + skrót miejscowości np.: A.
        for litera in litery:
            patterns.append([{"LEMMA":"sędzia"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"sędzia"}, {"LOWER":"w"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ", "OP":"+"}, {"LOWER":"w"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"sędzia"}, {"LEMMA":"sąd"}, {"POS":"ADJ", "OP":"+"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])

    return patterns
