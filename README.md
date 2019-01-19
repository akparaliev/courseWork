# Project Name 
Coreference Resolution NLP  
# Project Goals
The task of the project is to find all expressions that refer to the same entity in a text. In other words 
the programm will detect a pronoun in a corpus and replace it with a related name. Futhermore, the next step 
will convert the preprocessed text into the Word2vec or Fast text format model. Afterwards evaluate the results. https://docs.google.com/spreadsheets/d/14hkjaUCk6k9vpKR2vDQGY39noIUAK24ks50MA6f6gLA/edit#gid=668610076-achieved 

# Project Steps
- splitting ASOIF and HP into paragraphs and preprocess them
- pronouns replacement
- train word embeddings models 
 https://github.com/gwohlgen/digitalhumanities_dataset_and_eval
- model saving
- Evaluation with doesnt_match_evaluation.py and analogies_evaluation.py scripts
- model saving
- statistics gathering
### Statistical Analysis
- ![does not match asessment table](https://github.com/akparaliev/courseWork/tree/master/images/d`tmtch.png)
- ![corpus size asessment table](https://github.com/akparaliev/courseWork/tree/master/images/corpus_size.jpg)
- ![frequency check asessment table](https://github.com/akparaliev/courseWork/tree/master/images/check_freq.jpg)
- ![b3_metrics asessment table](https://github.com/akparaliev/courseWork/tree/master/images/b3_metrics.jpg)
- ![analogies asessment table](https://github.com/akparaliev/courseWork/tree/master/images/analogies.jpg)


# project structure
- folder results contains assessment for doesn't match and analogies evaluation for 80 models
- tmp folder contains 80 models and files with preprocessed and corefed text
- milestone-one.py script processes text files and generates models
- coref_gold_standard.py script for calculating B3 metric, to determine whether the mentioned pairs are coreferent

### Requirements
- Python 3
- Nltk
- Spacy
- NeuralCoref
- Gensim
- NumPy


## milestone-one.py
### 3 functions:
#### preprocessFile(filePath, outputFilePath)
- filePath - path to your text(examples: hp.txt or asoif.txt)
- outputFilePath - where your preprocessed text will be saved
#### executeCoref(sentenceCount, targetTextPath, outputFilePath)
- sentenceCount - count of sentences that each paragraph has
- targetTextPath - path to your text(in task case - path to preprocessed text)
- outputFilePath - where your corefed text will be saved
#### trainText8CorpusModelAndSave(filePath, outputFilePath, kwargs)
- filePath - path to your text(in task case - path to corefed text)
- outputFilePath - where your model will be saved, this file is in vec format
- kwargs - arguments for text8corpus method
- usage: trainText8CorpusModelAndSave(BOOK+ '_corefed.txt', BOOK + '_corefed.model', cbow_mean=0,min_count=5,size=300, window=5, negative=0, hs=1, sample=0.001,workers=12)
#### trainFastTextAndSave(filePath, outputFilePath, kwargs)
- filePath - path to your text(in task case - path to corefed text)
- outputFilePath - where your model will be saved, this file is in vec format
- kwargs - arguments for FastText method
usage: trainFastTextAndSave(BOOK+ '_preprocessed.txt', BOOK + '_preprocessed_fast_text.model', size = 80)

## run doesn't match or analogies script
- clone this repo: https://github.com/gwohlgen/digitalhumanities_dataset_and_eval/
- put model to models folder
- and run scripts from src folder

## coref_gold_standard.py
- usage:
   - variable paragraph = "Hermione opened her mouth to argue, but at that moment Crookshanks leapt lightly onto her lap. A large, dead spider was dangling from his mouth."; - text
   - variable gold_clusters = [{'Hermione': {'Hermione ': [0], 'her': [2, 15]}, 'Crookshanks': {'Crookshanks': [11], 'his': [26]}  }]; - mentions and their positions
   - run executeParagraph(paragraph, gold_clusters) to see the results





