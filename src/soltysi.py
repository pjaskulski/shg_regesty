""" definicja reguł dla wyszukiwania urzedów w SHG """


def rule_patterns(slownik:str ='') -> list:
    """ definicje reguł """
    patterns = [
        # sołtys + przymiotnik (lub parę przymiotników)
        [{"LEMMA":"sołtys"}, {"POS":"ADJ", "OP": "+"}],
        [{"LEMMA":"sołtyska"}, {"POS":"ADJ", "OP": "+"}],
        # sołtys + przymiotnik i przymiotnik
        [{"LEMMA":"sołtys"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LEMMA":"sołtyska"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        # sołtys + nazwa własna (lub parę nazw)
        [{"LEMMA":"sołtys"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"sołtyska"}, {"POS":"PROPN", "OP": "+"}],
        # sołtys + przymiotnik + nazwa własna (lub parę nazw)
        [{"LEMMA":"sołtys"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"sołtyska"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        # sołtys + rzeczownik
        [{"LEMMA":"sołtys"}, {"POS":"NOUN"}],
        [{"LEMMA":"sołtyska"}, {"POS":"NOUN"}],
        # sołtys w nazwa (lub parę)
        [{"LEMMA":"sołtys"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"sołtyska"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        # sołtys z nazwa
        [{"LEMMA":"sołtys"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"sołtyska"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        # sołtys wsi nazwa
        [{"LEMMA":"sołtys"}, {"LOWER":"wsi"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"sołtyska"}, {"LOWER":"wsi"}, {"POS":"PROPN", "OP": "+"}],
        # sołtys z wsi nazwa
        [{"LEMMA":"sołtys"}, {"LOWER":"z"}, {"LOWER":"wsi"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"sołtyska"}, {"LOWER":"z"}, {"LOWER":"wsi"}, {"POS":"PROPN", "OP": "+"}],
        # sołtys ze wsi nazwa
        [{"LEMMA":"sołtys"}, {"LOWER":"ze"}, {"LOWER":"wsi"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"sołtyska"}, {"LOWER":"ze"}, {"LOWER":"wsi"}, {"POS":"PROPN", "OP": "+"}],
        
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
        # sołtys + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"sołtys"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"sołtyska"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # sołtys + 'z' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"sołtys"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"sołtyska"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # sołtys + 'w' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"sołtys"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"sołtyska"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])

        # sołtys z + skrót miejscowości np.: A.
        for litera in litery:
            patterns.append([{"LEMMA":"sołtys"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"sołtyska"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])

    return patterns
