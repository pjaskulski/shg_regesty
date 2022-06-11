""" definicja reguł dla wyszukiwania urzedów w SHG """

# rajca + przymiotnik (lub parę przymiotników) np. rajca krakowski
# rajca + przymiotnik i przymiotnik np. rajcy starzy i nowi
# rajca + nazwa własna (lub parę nazw) np. rajca Wiślicy
# rajca + skrót (geograficzny) np rajca krak., rajcy biec. rajców lel.
# rajca w nazwa np. rajca w Wiślicy
# rajca z nazwa np. rajca z Wiślicy
# rajca m. nazwa np. rajca m. Wiślicy

def rule_patterns() -> list:
    """ definicje reguł """
    patterns = [
        # rajca + przymiotnik (lub parę przymiotników)
        [{"LEMMA":"rajca"}, {"POS":"ADJ", "OP": "+"}],
         # rajca + przymiotnik i przymiotnik
        [{"LEMMA":"rajca"}, {"POS":"ADJ"}, {"LOWER":"i"}, {"POS":"ADJ"}],
        # rajca + nazwa własna (lub parę nazw)
        [{"LEMMA":"rajca"}, {"POS":"PROPN", "OP": "+"}],
        # rajca + rzeczownik
        [{"LEMMA":"rajca"}, {"POS":"NOUN"}],
        # rajca + skrót (geograficzny) np krak. biec. lel.
        [{"LEMMA":"rajca"}, {"LOWER":"krak"}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"lel"}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"biec"}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"chęc."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"czchow."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"czech."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"czes."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"frank."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"gnieźn."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"imbr."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"jędrz."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"kal."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"Klar."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"koprz."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"krak."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"ksiąs."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"lel."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"lub."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"łęcz."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"magd."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"maz."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"miech."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"miej."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"mog."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"mstow."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"niem."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"opocz."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"ośw."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"pilzn."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"pol."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"poł."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"pozn."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"pras."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"prosz."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"przem."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"rad."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"roz."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"san."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"sand."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"sądec."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"sieciech."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"sier."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"siew."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"staniąt."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"starosądec."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"szczyrz."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"śl."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"średz."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"świętokrz."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"świętop."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"tyn."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"wąch."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"węg."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"wiel."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"wiśl."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"wojn."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"zator."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"zawich."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"zwierzyn."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"żarn."}, {"IS_PUNCT":True}],
        [{"LEMMA":"rajca"}, {"LOWER":"żyd."}, {"IS_PUNCT":True}],
        # rajca w nazwa (lub parę)
        [{"LEMMA":"rajca"}, {"LOWER":"w"}, {"POS":"PROPN", "OP": "+"}],
        # rajca z nazwa
        [{"LEMMA":"rajca"}, {"LOWER":"z"}, {"POS":"PROPN", "OP": "+"}],
         # rajca m. nazwa
        [{"LEMMA":"rajca"}, {"LOWER":"m"}, {"IS_PUNCT":True}, {"POS":"PROPN", "OP": "+"}],
    ]
    return patterns


def short_dict() -> dict:
    """ definicje skrótów dla słownika krakowskiego """
    result = {
        "biec.":"biecki",
        "chęc.":"chęciński",
        "czchow.":"czchowski",
        "czech.":"czechowski",
        "czes.":"czeski",
        "frank.":"frankoński",
        "gnieźn.":"gnieźnieński",
        "imbr.":"imbramowicki",
        "jędrz.":"jędrzejowski",
        "kal.":"kaliski",
        "Klar.":"Klaryski",
        "koprz.":"koprzywnicki",
        "krak.":"krakowski",
        "ksiąs.":"ksiąski",
        "lel.":"lelowski",
        "lub.":"lubelski",
        "łęcz.":"łęczycki",
        "magd.":"magdeburski",
        "maz.":"mazowiecki",
        "miech.":"miechowski",
        "miej.":"miejski",
        "mog.":"mogilski",
        "mstow.":"mstowski",
        "niem.":"niemiecki",
        "opocz.":"opoczyński",
        "ośw.":"oświęcimski",
        "pilzn.":"pilzneński",
        "pol.":"polski",
        "poł.":"połaniecki",
        "pozn.":"poznański",
        "pras.":"praskie",
        "prosz.":"proszowski",
        "przem.":"przemyski",
        "rad.":"radomski",
        "roz.":"rozpierski",
        "san.":"sanocki",
        "sand.":"sandomierski",
        "sądec.":"sądecki",
        "sieciech.":"sieciechowski",
        "sier.":"sieradzki",
        "siew.":"siewierski",
        "staniąt.":"staniątecki",
        "starosądec.":"starosądecki",
        "szczyrz.":"szczyrzycki",
        "śl.":"śląski",
        "średz.":"średzki",
        "świętokrz.":"świętokrzyski",
        "świętop.":"świętopietrze",
        "tyn.":"tyniecki",
        "wąch.":"wąchocki",
        "węg.":"węgierski",
        "wiel.":"wieluński",
        "wiśl.":"wiślicki",
        "wojn.":"wojnicki",
        "zator.":"Zatorski",
        "zawich.":"zawichojski",
        "zwierzyn.":"zwierzyniecki",
        "żarn.":"żarnowski",
        "żyd.":"żydowski",
    }

    return result 