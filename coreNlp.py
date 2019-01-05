import en_coref_md
import numpy as np
from pprint import pprint
from pynlp import StanfordCoreNLP
def executeParagraphPyNlp(par):
    annotators = 'coref'
    options = {'openie.resolve_coref': True}
    nlp = StanfordCoreNLP(annotators=annotators, options=options)
    doc = nlp(par)
    print(doc)

paragraph = "Hermione opened her mouth to argue, but at that moment Crookshanks leapt lightly onto her lap. A large, dead spider was dangling from his mouth."
executeParagraphPyNlp(paragraph)