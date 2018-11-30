import nltk
from nltk.corpus import stopwords
from gensim.models import word2vec
from nltk.corpus import gutenberg
import en_coref_md
import string

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
        current_paragraph_sentences.append(sentences[index])
        if (len(current_paragraph_sentences) == sentenceCount or len(sentences)-1==index):
            paragraph = " ".join(current_paragraph_sentences)
            doc = nlp(paragraph)
            corefed_sentences.append(doc._.coref_resolved)
            current_paragraph_sentences = []

    outputFile = open(outputFilePath, 'wt', encoding='UTF8')
    outputFile.writelines(line + '\n' for line in corefed_sentences)
    outputFile.close()

def trainModelAndSave(filePath, outputFilePath):
    with open(filePath, encoding='utf-8') as file:
        content = file.read()
    sentences = word2vec.Text8Corpus(filePath)
    model = word2vec.Word2Vec(sentences, cbow_mean=0, min_count=5, size=300, window=5, negative=0, hs=1, sample=0.001,
                             workers=12)
    model.wv.save_word2vec_format(outputFilePath, binary=False)


#model = trainModelAndSave('./hp_4_sentences_split.txt')
#model.wv.save_word2vec_format("./digitalhumanities_dataset_and_eval/models/hp_4_sentences_split.model", binary=False)

preprocessFile('./book_combined_sentences.txt','hp_preprocessed.txt')
executeCoref(4, './hp_preprocessed.txt', 'hp_corefed.txt')
trainModelAndSave('./hp_corefed.txt', './digitalhumanities_dataset_and_eval/models/hp_corefed.model')