import nltk
from nltk.corpus import stopwords
from gensim.models import word2vec
from nltk.corpus import gutenberg
import en_coref_md
import numpy as np
from pprint import pprint
from pynlp import StanfordCoreNLP

def evaluate_clusters(doc, current_gold):
    # clusters "mains" found by spacy
    current_doc_mains = [c.main.string for c in doc._.coref_clusters]
    print('\ncurrent_doc_mains:', current_doc_mains)

    # this will contrain: (len(gold_mentions), precision, recall, f1)
    cluster_results = []

    for gold_main, gold_mentions in current_gold.items():
        print('gold_main', gold_main)

        # 1.) find if the gold_main is in the document custering
        gold_in_spacy, found_cluster = False, None

        for cluster in doc._.coref_clusters:
            if cluster.main.string.strip() == gold_main.strip():
                print('Found cluster main:', gold_main)
                gold_in_spacy = True
                found_cluster = cluster

        if gold_in_spacy:
            ## precision: number of cluster_items which are in the gold cluster
            ## TODO .. extend this to check for the spans of mentions
            print('Mentions founded')
            for mention in found_cluster.mentions:
                print(mention.string.strip(), mention.start)

            found_mentions = [mention for mention in found_cluster.mentions
                              if mention.string.strip() in gold_mentions.keys()
                              and mention.start in gold_mentions[mention.string.strip()]]

            # print('found_mentions', found_mentions)
            precision = len(found_mentions) / len(found_cluster.mentions)
            recall = len(found_mentions) / len(gold_mentions)
            f1 = 2 * (precision * recall) / (precision + recall)
            print('P, R, F1:', precision, recall, f1)

            cluster_results.append((len(gold_mentions), precision, recall, f1))
        else:
            ## TODO add zero result for Precision and Recall for this cluster
            cluster_results.append((len(gold_mentions), 0, 0, 0))

    pprint(cluster_results)

    ## compute final b-cubed
    b3_avg = np.mean([f1 for _, _, _, f1 in cluster_results])
    print('b3_avg', b3_avg)

    total_num_gold = np.sum([len(gold_mentions) for gold_main, gold_mentions in current_gold.items()])
    b3_weighted = np.sum([f1 * len_gold / total_num_gold for len_gold, _, _, f1 in cluster_results])
    print('b3_weighted', b3_weighted)


def executeParagraph(par, gold_clusters):
    nlp = en_coref_md.load()
    doc = nlp(par)
    print(doc._.coref_resolved)
    print(doc._.coref_clusters)
    evaluate_clusters(doc, gold_clusters[0])

## define the gold clusters for all your selected paragraphs
paragraph = "Hermione opened her mouth to argue, but at that moment Crookshanks leapt lightly onto her lap. A large, dead spider was dangling from his mouth."
gold_clusters = [{'Hermione': {'Hermione ': [0], 'her': [2, 15]}, 'Crookshanks': {'Crookshanks': [11], 'his': [26]}  }]


executeParagraph(paragraph, gold_clusters)
