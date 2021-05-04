import unidecode
import regex as re
import spacy

class UtilisNLP():
    def __init__(self):
        self.nlp = spacy.load("es_core_news_md")

    def prprocessor(self,sentence,unCaptialize=True,delSymbols=True,delDigits=True,delAccents=True,lemma=True,delStops=True,stopWords=["PRON","DET","CCONJ","ADP"]):
        if unCaptialize:
            sentence = sentence.lower()
        if delAccents:
            sentence = unidecode.unidecode(sentence)
        if delSymbols:
            sentence = re.sub('[^\w]', " ", sentence)
        if delDigits:
            sentence = re.sub('\d', " ", sentence)
        doc = self.nlp(sentence)
        concatText = ""
        if not delStops:
            stopWords=[]
        for part in doc:
            if part.pos_ not in stopWords:
                if lemma:
                    concatText += part.lemma_+" "
                else:
                    concatText += part.text
        concatText = " ".join(concatText.split())
        return concatText

def main():
    text="Este es un texto de ejemplo, podemos eliminar tildes áé, etc... y mucho mas incluso digitos como el 1,2,3,4,5 y lematizar"
    print(text)
    utilis=UtilisNLP()
    print(utilis.prprocessor(text))

if __name__ == "__main__":
    main()
