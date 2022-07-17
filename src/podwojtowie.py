""" definicja reguł dla wyszukiwania urzedów w SHG """


def rule_patterns(slownik:str ='') -> list:
    """ definicje reguł """
    patterns = [
        # podwójt + przymiotnik (lub parę przymiotników)
        [{"LEMMA":"podwójt"}, {"POS":"ADJ", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"POS":"ADJ", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"POS":"ADJ", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"POS":"ADJ", "OP": "+"}],
        [{"LOWER":"landwójt"}, {"POS":"ADJ", "OP": "+"}],
        [{"LOWER":"landwójta"}, {"POS":"ADJ", "OP": "+"}],
        [{"LOWER":"landwójtem"}, {"POS":"ADJ", "OP": "+"}],
        [{"LOWER":"landwójtowi"}, {"POS":"ADJ", "OP": "+"}],
        [{"LEMMA":"wicesołtys"}, {"POS":"ADJ", "OP": "+"}],
        # podwójt + przymiotnik i przymiotnik
        [{"LEMMA":"podwójt"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LOWER":"podwójci"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LEMMA":"podwójtowy"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LEMMA":"podwójcina"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LEMMA":"landwójt"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LOWER":"landwójta"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LOWER":"landwójtem"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LOWER":"landwójtowi"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        [{"LEMMA":"wicesołtys"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        # podwójt + nazwa własna (lub parę nazw)
        [{"LEMMA":"podwójt"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"landwójt"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójta"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtem"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtowi"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wicesołtys"}, {"POS":"PROPN", "OP": "+"}],
        # podwójt + przymiotnik + nazwa własna (lub parę nazw)
        [{"LEMMA":"podwójt"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"landwójt"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójta"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtem"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtowi"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wicesołtys"}, {"POS":"ADJ"}, {"POS":"PROPN", "OP": "+"}],
        # podwójt + rzeczownik
        [{"LEMMA":"podwójt"}, {"POS":"NOUN"}],
        [{"LOWER":"podwójci"}, {"POS":"NOUN"}],
        [{"LEMMA":"podwójtowy"}, {"POS":"NOUN"}],
        [{"LEMMA":"podwójcina"}, {"POS":"NOUN"}],
        [{"LEMMA":"landwójt"}, {"POS":"NOUN"}],
        [{"LOWER":"landwójta"}, {"POS":"NOUN"}],
        [{"LOWER":"landwójtem"}, {"POS":"NOUN"}],
        [{"LOWER":"landwójtowi"}, {"POS":"NOUN"}],
        [{"LEMMA":"wicesołtys"}, {"POS":"NOUN"}],
        # podwójt w nazwa (lub parę)
        [{"LEMMA":"podwójt"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"landwójt"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójta"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtem"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtowi"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wicesołtys"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        # podwójt z nazwa
        [{"LEMMA":"podwójt"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"landwójt"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójta"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtem"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtowi"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wicesołtys"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
        # podwójt m. nazwa
        [{"LEMMA":"podwójt"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"landwójt"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójta"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtem"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtowi"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wicesołtys"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
        # podwójt miasta nazwa
        [{"LEMMA":"podwójt"}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"landwójt"}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójta"}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtem"}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtowi"}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wicesołtys"}, {"LEMMA":"miasto"}, {"POS":"PROPN", "OP": "+"}],
        # podwójt wsi nazwa
        [{"LEMMA":"podwójt"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"landwójt"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójta"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtem"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtowi"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wicesołtys"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        # podwójt z wsi nazwa
        [{"LEMMA":"podwójt"}, {"LOWER":"z"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LOWER":"z"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LOWER":"z"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LOWER":"z"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"landwójt"}, {"LOWER":"z"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójta"}, {"LOWER":"z"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtem"}, {"LOWER":"z"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"landwójtowi"}, {"LOWER":"z"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wicesołtys"}, {"LOWER":"z"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        # podwójt ze wsi nazwa
        [{"LEMMA":"podwójt"}, {"LOWER":"ze"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LOWER":"podwójci"}, {"LOWER":"ze"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójtowy"}, {"LOWER":"ze"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"podwójcina"}, {"LOWER":"ze"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"landwójt"}, {"LOWER":"ze"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        [{"LEMMA":"wicesołtys"}, {"LOWER":"ze"}, {"LEMMA":"wieś"}, {"POS":"PROPN", "OP": "+"}],
        # podwójt sądu wyższego pr. niem.
        [{"LEMMA":"podwójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        [{"LOWER":"podwójci"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        # podwójt sądu leńskiego + nazwa (opcjonalnie - w)
        [{"LEMMA":"podwójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"w", "OP":"?"}, {"POS":"PROPN"}],
        [{"LOWER":"podwójci"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"w", "OP":"?"}, {"POS":"PROPN"}],
        [{"LEMMA":"podwójt"}, {"LEMMA":"sąd"}, {"LEMMA":"leński"}, {"LOWER":"w", "OP":"?"}, {"POS":"PROPN"}],
        [{"LOWER":"podwójci"}, {"LEMMA":"sąd"}, {"LEMMA":"leński"}, {"LOWER":"w", "OP":"?"}, {"POS":"PROPN"}],
        # podwójt sądu leńskiego + nazwa (opcjonalnie - z)
        [{"LEMMA":"podwójt"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"z", "OP":"?"}, {"POS":"PROPN"}],
        [{"LOWER":"podwójci"}, {"LEMMA":"sąd"}, {"POS":"ADJ"}, {"LOWER":"z", "OP":"?"}, {"POS":"PROPN"}],
        [{"LEMMA":"podwójt"}, {"LEMMA":"sąd"}, {"LEMMA":"leński"}, {"LOWER":"z", "OP":"?"}, {"POS":"PROPN"}],
        [{"LOWER":"podwójci"}, {"LEMMA":"sąd"}, {"LEMMA":"leński"}, {"LOWER":"z", "OP":"?"}, {"POS":"PROPN"}],
        # podwójt leńskiego sądu
        [{"LEMMA":"podwójt"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"LOWER":"w", "OP":"?"}, {"POS":"PROPN"}],
        # landwójt sądu pr. niem. + nazwa
        [{"LEMMA":"landwójt"}, {"LEMMA":"sąd"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w", "OP":"?"}, {"POS":"PROPN"}],
        [{"LOWER":"landwójta"}, {"LEMMA":"sąd"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w", "OP":"?"}, {"POS":"PROPN"}],
        [{"LOWER":"landwójtem"}, {"LEMMA":"sąd"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w", "OP":"?"}, {"POS":"PROPN"}],
        [{"LOWER":"landwójtowi"}, {"LEMMA":"sąd"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w", "OP":"?"}, {"POS":"PROPN"}],
        # landwójt sądu prawa niem. + nazwa
        [{"LEMMA":"landwójt"}, {"LEMMA":"sąd"}, {"LOWER":"prawa"}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w", "OP":"?"}, {"POS":"PROPN"}],
        [{"LOWER":"landwójta"}, {"LEMMA":"sąd"}, {"LOWER":"prawa"}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w", "OP":"?"}, {"POS":"PROPN"}],
        [{"LOWER":"landwójtem"}, {"LEMMA":"sąd"}, {"LOWER":"prawa"}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w", "OP":"?"}, {"POS":"PROPN"}],
        [{"LOWER":"landwójtowi"}, {"LEMMA":"sąd"}, {"LOWER":"prawa"}, {"LOWER":"niem"}, {"IS_PUNCT":True}, {"LOWER":"w", "OP":"?"}, {"POS":"PROPN"}],
        # podwójci wyższego sądu [prawa niem.]
        [{"LOWER":"podwójci"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"IS_PUNCT":True, "OP":"?"}, {"LEMMA":"prawo"}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        [{"LOWER":"podwójci"}, {"LEMMA":"wysoki"}, {"LEMMA":"sąd"}, {"IS_PUNCT":True, "OP":"?"}, {"LEMMA":"prawo"}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        [{"LOWER":"podwójci"}, {"POS":"ADJ"}, {"LEMMA":"sąd"}, {"IS_PUNCT":True, "OP":"?"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
        [{"LOWER":"podwójci"}, {"LEMMA":"wysoki"}, {"LEMMA":"sąd"}, {"IS_PUNCT":True, "OP":"?"}, {"LOWER":"pr"}, {"IS_PUNCT":True}, {"LOWER":"niem"}, {"IS_PUNCT":True}],
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
        # podwójt + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"podwójt"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójci"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójtowy"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójcina"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"landwójt"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"landwójta"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"landwójtem"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"landwójtowi"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wicesołtys"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # podwójt + 'z' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"podwójt"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójci"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójtowy"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójcina"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"landwójt"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"landwójta"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"landwójtem"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"landwójtowi"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wicesołtys"}, {"LOWER":"z"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # podwójt + 'w' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"podwójt"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójci"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójtowy"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójcina"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"landwójt"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"landwójta"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"landwójtem"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"landwójtowi"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wicesołtys"}, {"LOWER":"w"}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        # podwójt + 'm' + skrót (geograficzny) np krak. biec. lel.
        patterns.append([{"LEMMA":"podwójt"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"podwójci"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójtowy"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"podwójcina"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"landwójt"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"landwójta"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"landwójtem"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LOWER":"landwójtowi"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])
        patterns.append([{"LEMMA":"wicesołtys"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"LOWER":f"{shortcut}"}, {"IS_PUNCT":True}])

        # podwójt z + skrót miejscowości np.: A.
        for litera in litery:
            patterns.append([{"LEMMA":"podwójt"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LOWER":"podwójci"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"podwójt"}, {"LEMMA":"wieś"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LOWER":"podwójci"}, {"LEMMA":"wieś"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"podwójt"}, {"LEMMA":"miasto"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LOWER":"podwójci"}, {"LEMMA":"miasto"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"podwójtowy"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"podwójcina"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"landwójt"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LOWER":"landwójta"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LOWER":"landwójtem"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LOWER":"landwójtowi"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"landwójt"}, {"LEMMA":"wieś"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LOWER":"landwójta"}, {"LEMMA":"wieś"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LOWER":"landwójtem"}, {"LEMMA":"wieś"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LOWER":"landwójtowi"}, {"LEMMA":"wieś"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"wicesołtys"}, {"LOWER":"z"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])
            patterns.append([{"LEMMA":"wicesołtys"}, {"LEMMA":"wieś"}, {"TEXT":f"{litera}"}, {"IS_PUNCT":True}])

    return patterns
