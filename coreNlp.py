
#from pynlp import StanfordCoreNLP
from stanfordcorenlp import StanfordCoreNLP
import json

def getMainMention(mentions):
    for x in mentions:
        if x["isRepresentativeMention"] == True:
            return x["text"]
    return ""

def executeParagraphPyNlp(text):
    nlp = StanfordCoreNLP('http://localhost', port=9000)
    pros = {'annotators': 'coref', 'pinelineLanguage': 'en'}
    result_dict = json.loads(nlp.annotate(text, properties=pros))

    for idx, mentions in result_dict['corefs'].items():
        main_mention = getMainMention(mentions)
        for m in mentions:
            print(m)





def executeParagraphPynlp(par):
    annotators = 'coref'
    options = {'openie.resolve_coref': True}
    nlp = StanfordCoreNLP(annotators=annotators, options=options)
    doc = nlp(par)
    resolved = list(tok for tok in doc)
    print(doc)

paragraph = "Hermione opened her mouth to argue, but at that moment Crookshanks leapt lightly onto her lap. A large, dead spider was dangling from his mouth."
##executeParagraphPyNlp(paragraph)
import sys
print(sys.path)
sys.path.append("C:\\Users\\Nurbek_Akparaliev\\projects\\courseWork\\stanford-corenlp-python")
import jsonrpc