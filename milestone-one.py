import nltk
from nltk.corpus import stopwords
from gensim.models import word2vec
from nltk.corpus import gutenberg
import en_coref_md
import string
from gensim.models import FastText

def preprocessFile(filePath, outputFilePath):
    with open(filePath, encoding='utf-8') as file:
        content = file.read()
    filtered_sentences = []
    sentences = nltk.sent_tokenize(content)
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        if len(tokens) > 0:
            filtered_sentences.append(' '.join(tokens))

    outputFile = open(outputFilePath, 'wt', encoding='UTF8')
    outputFile.writelines(sentence + '.\n' for sentence in filtered_sentences)
    outputFile.close()


def executeCoref(sentenceCount, targetTextPath, outputFilePath):
    nlp = en_coref_md.load()
    with open(targetTextPath, encoding='utf-8') as file:
        content = file.read()
    corefed_sentences = []
    sentences = nltk.sent_tokenize(content)

    current_paragraph_sentences = []

    for index in range(len(sentences)):
        if index % 25 == 0:
            print('Sentences done: %d of %d' % (index, len(sentences)))

        current_paragraph_sentences.append(sentences[index])
        if (len(current_paragraph_sentences) == sentenceCount or len(sentences)-1==index):
            paragraph = " ".join(current_paragraph_sentences)
            doc = nlp(paragraph)
            corefed_sentences.append(doc._.coref_resolved)
            current_paragraph_sentences = []

    outputFile = open(outputFilePath, 'wt', encoding='UTF8')
    outputFile.writelines(line + '\n' for line in corefed_sentences)
    outputFile.close()

def trainText8CorpusModelAndSave(filePath, outputFilePath, **kwargs):
    with open(filePath, encoding='utf-8') as file:
        content = file.read()
    sentences = word2vec.Text8Corpus(filePath)
    model = word2vec.Word2Vec(sentences, **kwargs)
    model.wv.save_word2vec_format(outputFilePath, binary=False)

def trainFastTextAndSave(filePath, outputFilePath, **kwargs):
    with open(filePath, encoding='utf-8') as file:
        content = file.read()
    sentences = word2vec.Text8Corpus(filePath)
    model = FastText(sentences, **kwargs)
    model.wv.save_word2vec_format(outputFilePath, binary=False)
    #sentences = word2vec.Text8Corpus(filePath)

    #model = FastText(sentences, min_count=5, size=300, window=5, workers=12, hs=1, sample=0.001, cbow_mean=0)
    #model.save(outputFilePath, binary=False)
def evaluateSentence(sentence):
    nlp = en_coref_md.load()
    doc = nlp(sentence)
    print(doc._.coref_resolved)

BOOK = 'tmp/soiaf4books'
#preprocessFile(BOOK + '.txt', BOOK+'_preprocessed.txt')
#executeCoref(4, BOOK+'_preprocessed.txt', BOOK+'_corefed.txt')
#trainText8CorpusModelAndSave(BOOK+ '_corefed.txt', BOOK + '_corefed.model', cbow_mean=0,min_count=5,size=300, window=5, negative=0, hs=1, sample=0.001,workers=12)
#trainFastTextAndSave(BOOK+ '_preprocessed.txt', BOOK + '_preprocessed_fast_text.model', size = 80)
#evaluateSentence('Well, we were always going to fail that one,” said Ron gloomily as they ascended the marble staircase, Ron had just made Harry feel rather better by telling Harry how Ron told the examiner in detail about the ugly man with a wart on his nose in his crystal ball, only to look up and realize Ron had been describing his examiner’s reflection.')

