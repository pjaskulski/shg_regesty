""" Analiza występowania i tagowania jednostek monetarnych - test """
import spacy
from spacy.matcher import Matcher


def rule_patterns() -> list:
    """ definicje reguł """
    coin_patterns = [
        [{"POS":"ADJ"}, {"LOWER":"zł"}], # czerwony zł
        [{"POS":"ADJ"}, {"LOWER":"fl"}, {"IS_PUNCT":True}], # czerwony fl.
        [{"POS":"ADJ"}, {"LOWER":"fl"}, {"IS_PUNCT":True}, {"LOWER":"węg"}, {"IS_PUNCT":True}], # czerwony fl. węg.
        [{"LOWER":"fl"}, {"IS_PUNCT":True}, {"LOWER":"węg"}, {"IS_PUNCT":True}], # fl. węg.
        [{"POS":"ADJ"}, {"LOWER":"fl"}, {"IS_PUNCT":True}, {"POS":"ADJ"}], # czerwony fl. węgierski
        [{"LEMMA":"denar"}], # denar
        [{"LOWER":"den"}, {"IS_PUNCT":True}], # den.
        [{"LOWER":"den"}, {"IS_PUNCT":True}, {"LOWER":"chełm"}, {"IS_PUNCT":True}], # den. chełm.
        [{"LOWER":"den"}, {"IS_PUNCT":True}, {"LOWER":"kol"}, {"IS_PUNCT":True}], # den. kol.
        [{"LOWER":"den"}, {"IS_PUNCT":True}, {"LOWER":"lit"}, {"IS_PUNCT":True}], # den. lit.
        [{"LOWER":"den"}, {"IS_PUNCT":True}, {"POS":"ADJ"}], # den. litewski
        [{"LOWER":"fl"}, {"IS_PUNCT":True}],  # fl.
        [{"LOWER":"fl"}, {"IS_PUNCT":True}, {"LEMMA":"moneta"}, {"POS":"ADJ"}], # fl. monety polskiej
        [{"LOWER":"fl"}, {"IS_PUNCT":True}, {"LOWER":"pol"}, {"IS_PUNCT":True}], # fl. pol.
        [{"LOWER":"fl"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"LEMMA":"złoto"}], # fl. w złocie
        [{"LOWER":"fl"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"LOWER":"półgr"}, {"IS_PUNCT":True}], # fl. w półgr.
        [{"LOWER":"gr"}],
        [{"LOWER":"gr"}, {"POS":"ADJ"}], # grosz czeski, grosz praski, grosz litewski, grosz szeroki
        [{"LOWER":"gr"}, {"LOWER":"czes"}, {"IS_PUNCT":True}], # grosz czes.
        [{"LOWER":"gr"}, {"LOWER":"lit"}, {"IS_PUNCT":True}], # grosz lit.
        [{"LOWER":"gr"}, {"LOWER":"pras"}, {"IS_PUNCT":True}], # grosz pras.
        [{"LOWER":"gr"}, {"LOWER":"szer"}, {"IS_PUNCT":True}], # grosz szer.
        [{"LOWER":"gr"}, {"LEMMA":"moneta"}, {"POS":"ADJ"}], # gr monety krakowskiej, gr monety pospolitej
        [{"LOWER":"gr"}, {"LEMMA":"moneta"}, {"LOWER":"krak"}, {"IS_PUNCT":True}], # gr monety krak.
        [{"LOWER":"gr"}, {"LEMMA":"moneta"}, {"LOWER":"posp"}, {"IS_PUNCT":True}], # gr monety posp.
        [{"LOWER":"grz"}, {"IS_PUNCT":True}], # grz.
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"POS":"ADJ"}], # grz. czeska
        [{"LOWER":"grz"}, {"LOWER":""}],
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"gr"}], # grz. gr
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"gr"}, {"LOWER":"czes"}, {"IS_PUNCT":True}], # grz. gr czes.
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"gr"}, {"POS":"ADJ"}], # grz. gr czeskich, pospolitych
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"gr"}, {"LOWER":"posp"}, {"IS_PUNCT":True}], # grz. gr posp.
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"gr"}, {"LOWER":"pras"}, {"IS_PUNCT":True}], # grz. gr pras.
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"gr"}, {"LOWER":"szer"}, {"IS_PUNCT":True}], # grz. gr szer.
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LEMMA":"kwartnik"}], # grz. kwartników
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"POS":"ADJ"}, {"LEMMA":"moneta"}, {"LOWER":"krak"}, {"IS_PUNCT":True}], # grz. lepszej monety krak., pospolitej monety krak.
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LEMMA":"moneta"}, {"POS":"ADJ"}], # grz. monety obiegowej
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LEMMA":"moneta"}, {"LOWER":"posp"}, {"IS_PUNCT":True}],
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"POS":"ADJ"}, {"LEMMA":"moneta"}], # grz. obiegowej monety, pospolitej monety
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"półgr"}], # grz. półgr
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"półgr"}, {"POS":"ADJ"}], # grz. półgr polskich, szerokich, praskich
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"półgr"}, {"LOWER":"szer"}, {"IS_PUNCT":True}], # grz. półgr szer.
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"półgr"}, {"LOWER":"pol"}, {"IS_PUNCT":True}], # grz. półgr pol.
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"półgr"}, {"POS":"ADJ"}, {"LEMMA":"moneta"}, {"LOWER":"krak"}, {"IS_PUNCT":True}], # grz. półgr lepszej monety krak.
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LEMMA":"srebro"}], # grz. srebra
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"szer"}, {"IS_PUNCT":True}, {"LOWER":"gr"}], # grz. szer. gr
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"szer"}, {"IS_PUNCT":True}, {"LOWER":"gr"}, {"POS":"ADJ"}], # grz. szer. gr czeskich
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"szer"}, {"IS_PUNCT":True}, {"LEMMA":"kwartnik"}], # grz. szer. kwartników
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"szer"}, {"IS_PUNCT":True}, {"LOWER":"półgr"}, {"POS":"ADJ"}, {"LEMMA":"moneta"}, {"LOWER":"krak"}, {"IS_PUNCT":True}], # grz. szer. półgr większej monety krak.
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"POS":"ADJ"}, {"LOWER":"gr"}, {"LEMMA":"moneta"}, {"LOWER":"krak"}, {"IS_PUNCT":True}], # grz. średnich gr monety krak.
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"POS":"ADJ"}, {"LEMMA":"moneta"}], # grz. w bieżącej monecie
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"LEMMA":"grosz"}], # grz. w groszach
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"LEMMA":"kwartnik"}], # grz. w kwartnikach
        [{"LOWER":"grz"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"LEMMA":"moneta"}, {"POS":"ADJ"}], # grz. w monecie bieżącej, pospolitej
        [{"LEMMA":"kopa"}], # kopa [kop albo kóp]
        [{"LOWER":"kop"}], # kop
        [{"LOWER":"kóp"}], # kóp
        [{"LEMMA":"kopa"}, {"LOWER":"gr"}, {"LEMMA":"moneta"}, {"POS":"ADJ"}], # kopa gr monety bieżącej, pospolitej
        [{"LEMMA":"kopa"}, {"LOWER":"gr"}, {"LOWER":"w"}, {"LEMMA":"szeląg"}], # kopa gr w szelągach
        [{"LEMMA":"kopa"}, {"LEMMA":"kwartnik"}], # kopa kwartników
        [{"LEMMA":"kopa"}, {"LEMMA":"moneta"}, {"LOWER":"krak"}, {"IS_PUNCT":True}], # kopa monety krak.
        [{"LEMMA":"kopa"}, {"LEMMA":"moneta"}, {"POS":"ADJ"}], # kopa monety obiegowej
        [{"LEMMA":"kopa"}, {"LOWER":"półgr"}], # kopa półgr
        [{"LEMMA":"kopa"}, {"LOWER":"w"}, {"LEMMA":"moneta"}, {"POS":"ADJ"}], # kopa (kopy) w monecie pospolitej
        [{"LEMMA":"kopa"}, {"LOWER":"zł"}, {"IS_PUNCT":True}, {"LOWER":"pol"}, {"IS_PUNCT":True}], # kopa zł. pol.
        [{"LEMMA":"kopa"}, {"LOWER":"w"}, {"LOWER":"szer"}, {"IS_PUNCT":True}, {"LOWER":"gr"}, {"LOWER":"czes"},{"IS_PUNCT":True}], # kopy w szer. gr czes.
        [{"LEMMA":"kopa"}, {"LOWER":"w"}, {"LOWER":"szer"}, {"IS_PUNCT":True}, {"LOWER":"gr"}, {"POS":"ADJ"}], # kopy w szer. gr czeskich
        [{"LEMMA":"kwartnik"}], # kwartnik
        [{"LEMMA":"obol"}], # obol
        [{"LOWER":"ort"}], # ort
        [{"LEMMA":"pieniądz"}], # pieniądz
        [{"LOWER":"półgr"}], # półgr
        [{"LEMMA":"rubel"}], # rubel
        [{"LOWER":"sk"}, {"IS_PUNCT":True}], # sk.
        [{"LOWER":"sk"}, {"IS_PUNCT":True}, {"LOWER":"gr"}], # sk. gr czes.
        [{"LOWER":"sk"}, {"IS_PUNCT":True}, {"LOWER":"gr"}], # sk. gr czeskich
        [{"LOWER":"sk"}, {"IS_PUNCT":True}, {"LEMMA":"moneta"}, {"LOWER":"krak"}, {"IS_PUNCT":True}], # sk. monety krak.
        [{"LOWER":"sk"}, {"IS_PUNCT":True}, {"LEMMA":"moneta"}, {"POS":"ADJ"}], # sk. monety pospolitej
        [{"LEMMA":"solid"}], # solid
        [{"LOWER":"sz"}, {"IS_PUNCT":True}], # sz.
        [{"LEMMA":"szeląg"}], # szeląg
        [{"LEMMA":"szeląg"}, {"LOWER":"lit"}, {"IS_PUNCT":True}], # szeląg lit.
        [{"LOWER":"szer"}, {"IS_PUNCT":True}, {"LOWER":"gr"}, {"LOWER":"czes"}, {"IS_PUNCT":True}], # szer. gr czes.
        [{"LOWER":"szer"}, {"IS_PUNCT":True}, {"LOWER":"pras"}, {"IS_PUNCT":True}], # szer. gr pras.
        [{"LOWER":"ternar"}], # ternar
        [{"LOWER":"wiadr"}, {"IS_PUNCT":True}], # wiard.
        [{"LOWER":"wiadr"}, {"IS_PUNCT":True}, {"LOWER":"chełm"}, {"IS_PUNCT":True}, {"LEMMA":"moneta"}], # wiard. chełm. monety
        [{"LOWER":"wiadr"}, {"IS_PUNCT":True}, {"LEMMA":"moneta"}, {"POS":"ADJ"}], # wiard. monety pospolitej
        [{"LOWER":"wiadr"}, {"IS_PUNCT":True}, {"LEMMA":"moneta"}, {"LOWER":"tor"}, {"IS_PUNCT":True}], # wiard. monety tor.
        [{"LOWER":"wiadr"}, {"IS_PUNCT":True}, {"LOWER":"w"}, {"LOWER":"półgr"}], # wiard w półgr
        [{"LOWER":"zł"}, {"POS":"ADJ"}], # zł czerwony
        [{"LOWER":"zł"}, {"LOWER":"w"}, {"POS":"ADJ"}, {"LEMMA":"moneta"}], # zł w bieżącej monecie
        [{"LOWER":"zł"}, {"LOWER":"w"}, {"POS":"ADJ"}, {"LEMMA":"złoto"}], # zł w czystym złocie
        [{"LOWER":"zł"}, {"LOWER":"w"}, {"LOWER":"półgr"}, {"POS":"ADJ"}], # zł w półgr starych
        [{"LOWER":"zł"}, {"LOWER":"w"}, {"LEMMA":"złoto"}], # zł w złocie
        [{"LOWER":"zł"}, {"LOWER":"węg"}, {"IS_PUNCT":True}], # zł węg.
        [{"LOWER":"zł"}, {"IS_PUNCT":True}, {"POS":"ADJ"}, {"LOWER":"węg"}, {"IS_PUNCT":True}], # zł. czerwony węg.
        [{"LOWER":"zł"}, {"IS_PUNCT":True}, {"LOWER":"lit"}, {"IS_PUNCT":True}], # zł. lit.
        [{"LOWER":"zł"}, {"IS_PUNCT":True}, {"LEMMA":"moneta"}, {"LOWER":"śl"}, {"IS_PUNCT":True}], # zł. monety śl.
        [{"LOWER":"zł"}, {"IS_PUNCT":True}, {"LOWER":"pol"}, {"IS_PUNCT":True}], # zł. pol.
        [{"LOWER":"złoty"}, {"LOWER":"fl"}, {"IS_PUNCT":True}], # złoty fl.
    ]
    return coin_patterns


if __name__ == "__main__":
    patterns = rule_patterns()

    nlp = spacy.load("pl_core_news_lg")
    matcher = Matcher(nlp.vocab)
    matcher.add("Monety", patterns=patterns)

    tekst = """Grzegorz z Białej zapłacił 10 czerwonych zł kupcowi za ziarno.
Jan Bycyński jest winien 1 czerwonego fl. księciu Zygmuntowi z Cieszyna a jeżeli
nie zapłaci do żniw to dług wzrośnie do 2 fl. monety polskiej. Wiadro owsa kosztuje
w Krakowie 1. den. litewskiego a wiadro żyta 2 den. lit. Naprawa młyna kosztowała
12 krakowskich zł i 2 denary dla mistrza Jana a prac. Maciej wziął 1 fl. węg.
Opat Józef nabył konia za 2 grz. monety obiegowej od kupca Likiera. Od tegoż kupca
nabył także za 2 grz. w groszach wóz siana dobrego. Z miasta Biała podatku 
3 kopy monety obiegowej i kopę kwartników. Abacy winien jest kupcom z Orawy 4 solidy za rzemienie,
kopę monety krak. za drewno, oraz grz. w monecie krakowskiej za dzierżawę wozów."""

    doc = nlp(tekst)
    matches = matcher(doc)

    # tylko nie zawierające się znaleziska
    spans = [doc[start:end] for _, start, end in matches]
    for span in spacy.util.filter_spans(spans):
        print(span.text)

# WYNIK:
# czerwonych zł
# czerwonego fl.
# fl. monety polskiej
# den. litewskiego
# den. lit.
# krakowskich zł
# denary
# fl. węg.
# grz. monety obiegowej
# grz. w groszach
# kopy monety obiegowej
# kopę kwartników
# solidy
# kopę monety krak.
# grz. w monecie krakowskiej