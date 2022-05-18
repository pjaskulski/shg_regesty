""" Analiza występowania i tagowania jednostek monetarnych - test """
import spacy
from spacy.matcher import Matcher
from monety import rule_patterns


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
kopę monety krak. za drewno, oraz grz. w monecie krakowskiej za dzierżawę wozów. 
Za przejazd mostem """

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
