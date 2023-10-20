import spacy
import json 

nlp = spacy.load("pt_textcat_demo8") #problemas no NLU com o modelo não reconhecer "online" e "web" como coisas de pesquisa_web



total_answers= 0
correct_answers =0 

with open("test.json") as f:
     data = json.load(f)

     for i in data["rasa_nlu_data"]["common_examples"]:
      frase= i["text"]
      frase = frase.lower()
      doc  = nlp(frase)
      predicted_category = max(doc.cats, key=doc.cats.get)
      correct_result = i["intent"]
      
      result_parsed = predicted_category
      if result_parsed == correct_result:
         correct_answers+=1  
      else: 
         print(  frase + "\n certa " +  str(correct_result) + " \n  " + str(result_parsed))  
         arrayProb= []   
         for key in doc.cats:
          arrayProb.append(doc.cats[key])  
         print(max(arrayProb))
      total_answers+=1

#resposta= modelo.get_classe(frase) #testar no codigo de routing uma probabilidade de 0.98 ou mais para ser aceito.

print( "total de questoes: " + str(total_answers))
print( "total de acertos: " + str(correct_answers))

