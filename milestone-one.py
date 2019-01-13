import nltk
from gensim.models import word2vec
import en_coref_md


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
    sentences = word2vec.Text8Corpus(filePath)
    model = word2vec.Word2Vec(sentences, **kwargs)
    model.wv.save_word2vec_format(outputFilePath, binary=False)

def trainFastTextAndSave(filePath, outputFilePath, **kwargs):
    sentences = word2vec.Text8Corpus(filePath)
    model = FastText(sentences, **kwargs)
    model.wv.save_word2vec_format(outputFilePath, binary=False)

def evaluateSentence(sentence):
    nlp = en_coref_md.load()
    doc = nlp(sentence)
    print(doc._.coref_resolved)

BOOK = 'tmp/soiaf4books'
#BOOK = 'tmp/hp'
#preprocessFile(BOOK + '.txt', BOOK+'_preprocessed.txt')
#executeCoref(500, BOOK+'_preprocessed.txt', BOOK+'_corefed_500.txt')
#trainText8CorpusModelAndSave(BOOK + '_preprocessed.txt', BOOK + '_preprocessed_text8_3.model', size=300, negative=15, sg=1, hs=1, iter=15, window=12)
#trainFastTextAndSave(BOOK + '_corefed_500.txt', BOOK + '_corefed_500_fasttext.model')
#evaluateSentence('Well, we were always going to fail that one,” said Ron gloomily as they ascended the marble staircase, Ron had just made Harry feel rather better by telling Harry how Ron told the examiner in detail about the ugly man with a wart on his nose in his crystal ball, only to look up and realize Ron had been describing his examiner’s reflection.')
evaluateSentence("Hermione opened her mouth to argue, but at that moment Crookshanks leapt lightly onto her lap. A large, dead spider was dangling from his mouth.")