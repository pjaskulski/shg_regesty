""" definicja reguł dla wyszukiwania urzedów w SHG """


def rule_patterns(slownik:str ='') -> list:
    """ definicje reguł """
    patterns = [
        # burmistrz + nazwa
        [{"LEMMA":"burmistrz"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"burm"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"POS":"PROPN", "OP": "+"}],
        # burmistrz + przymiotnik
        [{"LEMMA":"burmistrz"}, {"POS":"ADJ", "OP": "+"}],
        [{"LOWER":"burm."}, {"IS_PUNCT":True}, {"POS":"ADJ", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"POS":"ADJ", "OP": "+"}],
        # burmistrz miasteczka + nazwa
        [{"LEMMA":"burmistrz"}, {"LEMMA":"miasteczko"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LEMMA":"miasteczko"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"LEMMA":"miasteczko"}, {"POS":"PROPN", "OP": "+"}],
        # burmistrz miasta + nazwa
        [{"LEMMA":"burmistrz"}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        # burmistrz z +nazwa
        [{"LEMMA":"burmistrz"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        # burmistrz w +nazwa
        [{"LEMMA":"burmistrz"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        # burmistrz m. +nazwa
        [{"LEMMA":"burmistrz"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        # burm. + nazwa
        [{"LEMMA":"burm"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        # burmistrz miasta + nazwa
        [{"LEMMA":"burmistrz"}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"burmistrzowie"}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
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
        # burmistrz + skrót geogr.
        patterns.append([{"LEMMA":"burmistrz"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # burm. + skrót geogr.
        patterns.append([{"LOWER":"burm"}, {"IS_PUNCT":True},  {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])

        # burmistrz z + skrót miejscowości np.: burmistrz z A., burmistrz A.
        for litera in litery:
            patterns.append([{"LEMMA":"burmistrz"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"burmistrz"}, {"LOWER":"w"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"burmistrz"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LOWER":"burm"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LOWER":"burm"}, {"IS_PUNCT":True}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"burmistrzowie"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"burmistrzowie"}, {"LOWER":"w"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"burmistrzowie"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            


    return patterns
