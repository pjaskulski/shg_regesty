import spacy

nlp = spacy.load("pl_core_news_lg", exclude=["ner"])


#tekst = "1412 wójtowie i kuzyn landwójta Nowego Sącza i wójtowa Wioski wraz z wicesołtysem oraz landwójtem przekazują miejscowemu klasztorowi. Bycie wójtem to ważna funkcja, bycie wójtową też, można też być wójciną oraz pracowac jako landwójt."
tekst = "Jan notariusz kurii bpiej kupił wieś."
doc = nlp(tekst)

for token in doc:
    print(token.text, token.lemma_, token.pos_)

#for entity in doc.ents:
#    print(entity.text, entity.label_, spacy.explain(entity.label_))