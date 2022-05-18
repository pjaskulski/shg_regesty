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
        [{"":""}, {"":""}], # kopa gr monety bieżącej, pospolitej
        [{"":""}, {"":""}], # kopa gr w szelągach
        [{"":""}, {"":""}], # kopa kwartników
        [{"":""}, {"":""}], # kopa monety krak.
        [{"":""}, {"":""}], # kopa monety obiegowej
        [{"":""}, {"":""}], # kopa półgr
        [{"":""}, {"":""}], # kopa (kopy) w monecie pospolitej
        [{"":""}, {"":""}], # kopa zł. pol.
        [{"":""}, {"":""}], # kopy w szer. gr czes.
        [{"":""}, {"":""}], # kwartnik
        [{"":""}, {"":""}], # obol
        [{"":""}, {"":""}], # ort
        [{"":""}, {"":""}], # pieniądz
        [{"":""}, {"":""}], # półgr
        [{"":""}, {"":""}], # rubel
        [{"":""}, {"":""}], # sk.
        [{"":""}, {"":""}], # sk. gr czes.
        [{"":""}, {"":""}], # sk. gr czeskich
        [{"":""}, {"":""}], # sk. monety krak.
        [{"":""}, {"":""}], # sk. monety pospolitej
        [{"":""}, {"":""}], # solid
        [{"":""}, {"":""}], # sz.
        [{"":""}, {"":""}], # szeląg
        [{"":""}, {"":""}], # szeląg lit.
        [{"":""}, {"":""}], # szer. gr czes.
        [{"":""}, {"":""}], # szer. gr pras.
        [{"":""}, {"":""}], # ternar
        [{"":""}, {"":""}], # wiard.
        [{"":""}, {"":""}], # wiard. chełm. monety
        [{"":""}, {"":""}], # wiard. monety pospolitej
        [{"":""}, {"":""}], # wiard. monety tor.
        [{"":""}, {"":""}], # wiard w półgr
        [{"":""}, {"":""}], # zł czerwony
        [{"":""}, {"":""}], # zł w bieżącej monecie
        [{"":""}, {"":""}], # zł w czystym złocie
        [{"":""}, {"":""}], # zł w półgr starych
        [{"":""}, {"":""}], # zł w złocie
        [{"":""}, {"":""}], # zł węg.
        [{"":""}, {"":""}], # zł. czerwony węg.
        [{"":""}, {"":""}], # zł. lit.
        [{"":""}, {"":""}], # zł. monety śl.
        [{"":""}, {"":""}], # zł. pol.
        [{"":""}, {"":""}], # złoty fl.
        

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
nabył także za 2 grz. w groszach wóz siana dobrego."""

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
