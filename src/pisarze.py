""" definicja reguł dla wyszukiwania urzedów w SHG """


def rule_patterns(slownik:str ='') -> list:
    """ definicje reguł """
    patterns = [
        # pisarz m. + nazwa
        [{"LEMMA":"pisarz"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        # pisarz z + nazwa
        [{"LEMMA":"pisarz"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        # pisarz w + nazwa
        [{"LEMMA":"pisarz"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"pisarz"}, {"LOWER":"w"}, {"POS":"NOUN", "OP": "+"}],
        # pisarz miejski + nazwa
        [{"LEMMA":"pisarz"}, {"LEMMA":"miejski"}, {"POS":"PROPN", "OP": "+"}],
        # pisarz miej.
        [{"LEMMA":"pisarz"}, {"LOWER":"miej"}, {"IS_PUNCT":True}],
        # pisarz miej. + przymiotnik
        [{"LEMMA":"pisarz"}, {"LOWER":"miej"}, {"IS_PUNCT":True}, {"POS":"ADJ"}],
        # pisarz przymiotnik + nazwa
        [{"LEMMA":"pisarz"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        # pisarz sądu wyższego pr. niem.
        [{"LEMMA":"pisarz"}, {"LEMMA":"sąd"}, {"LEMMA":"wysoki"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        # pisarz + rzeczownik
        [{"LEMMA":"pisarz"}, {"POS":"NOUN", "OP":"+"}],
        # pisarz król.
        [{"LEMMA":"pisarz"}, {"LOWER":"król"}, {"IS_PUNCT":True}],
        # pisarz i dworzanin król.
        [{"LEMMA":"pisarz"}, {"LOWER":"i"}, {"POS":"NOUN"}, {"LOWER":"król"}, {"IS_PUNCT":True}],
        # pisarz kancelarii król.
        [{"LEMMA":"pisarz"}, {"POS":"NOUN"}, {"LOWER":"król"}, {"IS_PUNCT":True}],
        # pisarz star. + przymiotnik
        [{"LEMMA":"pisarz"}, {"LOWER":"star"}, {"IS_PUNCT":True}, {"POS":"ADJ"}],      
        # notariusz z + nazwa
        [{"LEMMA":"notariusz"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        # notariusz miejski w + nazwa, przymiotnik + nazwa, w rzeczownik
        [{"LEMMA":"notariusz"}, {"LEMMA":"miejski"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"notariusz"}, {"POS":"ADJ"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"notariusz"}, {"LOWER":"w"}, {"POS":"NOUN", "OP": "+"}],
        # notariusz z. sandomierskiej (przymiotnik)
        [{"LEMMA":"notariusz"}, {"LOWER":"z"}, {"IS_PUNCT":True}, {"POS":"ADJ"}],
        # notariusz + przymiotnik
        [{"LEMMA":"notariusz"}, {"POS":"ADJ"}],
        # notariusz + rzeczownik
        [{"LEMMA":"notariusz"}, {"POS":"NOUN", "OP":"+"}],
        # notariusz + rzeczownik + przymiotnik
        [{"LEMMA":"notariusz"}, {"POS":"NOUN"}, {"POS":"ADJ"}],
        # notariusz + król.
        [{"LEMMA":"notariusz"}, {"LOWER":"król"}, {"IS_PUNCT":True}],
        # notariusz + bpa
        [{"LEMMA":"notariusz"}, {"LOWER":"bpa"}],
        # notariusz i funkcja
        [{"LEMMA":"notariusz"}, {"LOWER":"i"}, {"POS":"NOUN"}],
        # notariusz + publ.
        [{"LEMMA":"notariusz"}, {"LOWER":"publ"}, {"IS_PUNCT":True}],
        # notariusz + kogo (np. Jana Długosza)
        [{"LEMMA":"notariusz"}, {"POS":"PROPN", "OP":"+"}],
        # notariusz + kogo (np. ks. Henryka)
        [{"LEMMA":"notariusz"}, {"LOWER":"ks"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP":"+"}],
        # notariusz w rzeczownik
        [{"LEMMA":"notariusz"}, {"LOWER":"w"}, {"POS":"NOUN", "OP":"+"}],
        # protonotariusz
        [{"LEMMA":"protonotariusz"}, {"LOWER":"król"}, {"IS_PUNCT":True}],
        [{"LEMMA":"protonotariusz"}, {"POS":"ADJ"}],
        [{"LEMMA":"protonotariusz"}, {"POS":"NOUN", "OP":"+"}],
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
        # pisarz + skrót geogr.
        patterns.append([{"LEMMA":"pisarz"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"LEMMA":"miejski"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"POS":"ADJ"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"POS":"NOUN"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"POS":"ADJ"}, {"LOWER":"ziemi"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"LEMMA":"sędzia"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"LOWER":"bpów"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"pisarz"}, {"LEMMA":"kapituła"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        
        # notariusz + skrót geogr.
        patterns.append([{"LEMMA":"notariusz"}, {"LOWER":"z"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"LOWER":"bpa"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"LOWER":"publ"}, {"IS_PUNCT":True}, {"POS":"NOUN"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"POS":"NOUN"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"LOWER":"kap"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"LOWER":"woj"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"notariusz"}, {"POS":"ADJ"}, {"LOWER":"w"}, {"LOWER":"diec"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        
        # pisarz z + skrót miejscowości np.: pisarz z A., pisarz A.
        for litera in litery:
            patterns.append([{"LEMMA":"pisarz"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"pisarz"}, {"LEMMA":"miejski"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"pisarz"}, {"POS":"ADJ"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"pisarz"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"pisarz"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"pisarz"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"pisarz"}, {"LOWER":"w"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"notariusz"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"notariusz"}, {"LOWER":"ze"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"notariusz"}, {"POS":"ADJ"}, {"LOWER":"w"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])

            

    return patterns
