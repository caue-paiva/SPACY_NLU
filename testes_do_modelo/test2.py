import spacy

nlp = spacy.load("pt_textcat_demo8")

doc = nlp("fale sobre a crise yanomami e traga fontes ")  #me de uma 

predicted_category = max(doc.cats, key=doc.cats.get)

print(predicted_category)

print(doc.cats)