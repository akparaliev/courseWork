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
   - does not match table
   <img src="/images/d`tmtch.png" alt="does not match table"/>
   
   - does not match diagramm hp 
   <img src="/images/5e1Go644cmI.jpg" width="700" height="400"  alt="does not match table"/>
   
   - does not match diagramm ASOIF
    <img src="/images/6PAatSy3mBU.jpg" width="700" height="400"  alt="does not match table"/>
    
   - analogies table 
   <img src="/images/analogies.jpg" alt="analogies"/>
   
   - analogies HP chart
   <img src="/images/LdsxuCMsfnk.jpg" width="700" height="400" alt="corpus size"/>
   
   - analogies ASOIF chart
   <img src="/images/o8QgVpfWO-w.jpg" width="700" height="400" alt="corpus size"/>
   
   - corpus size before and after coreference resolution table
   <img src="/images/corpus_size.jpg"  alt="corpus size"/>
   
   - corpus size before and after coreference resolution chart
   <img src="/images/Zzt6uGUIJYU.jpg" width="700" height="400" alt="corpus size"/>
   
   - check frequnecy table 
   <img src="/images/check_freq.jpg" alt="check_freq"/>
   
   - check frequency chart
   <img src="/images/mQ5ijx7ZifM.jpg" width="700" height="400" alt="corpus size"/>
   
   - b3 metrics table  Zzt6uGUIJYU.jpg
   <img src="/images/b3_metrics.jpg" alt="b3_metrics"/> 
   
    
#### Main Findings 
- as it seen from 'does not match table and does not match chart' the best accuracy for that task is to choose paragraph size = 500
- from the 'analogies table and chart' the best option for accuracy to take paragraph size = 50
- coreferencing resolution increases the size of corpus, but not dramatically 
- coreferencing resolution improves the acccuracy in both 'does not match' and 'analogies cases', but just for a tiny percentage 
- coref resolution depends on a text division, in order to achieve good percentage of accuracy it is better to choose reccomended settings as it was mentioned above
- Spacy makes a bunch of errors related to wrong indentification and pronoun replacement with frequence of 18%
- wrong recognition of the meaning of a text and incorrect with the nearest mention
- Wrong sex determination and incorrect recognition of inanimated pronouns 

all what is mentioned you can find following the link 
https://docs.google.com/spreadsheets/d/14hkjaUCk6k9vpKR2vDQGY39noIUAK24ks50MA6f6gLA/edit#gid=668610076




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
- variable paragraph = "Hermione opened her mouth to argue, but at that moment Crookshanks leapt lightly onto her lap. A large, dead spider was dangling from his mouth."; - text
- variable gold_clusters = [{'Hermione': {'Hermione ': [0], 'her': [2, 15]}, 'Crookshanks': {'Crookshanks': [11], 'his': [26]}  }]; - mentions and their positions
- run executeParagraph(paragraph, gold_clusters) to see the results

# Usage

- First, we should preprocess file, then evaluate coref resolution and train models 
```
BOOK = 'tmp/hp'
preprocessFile(BOOK + '.txt', BOOK+'_preprocessed.txt')
executeCoref(500, BOOK+'_preprocessed.txt', BOOK+'_corefed.txt')
trainText8CorpusModelAndSave(BOOK + '_corefed.txt', BOOK + '_corefed_text8.model', size=300, negative=15, sg=1, hs=1, iter=15, window=12)
trainFastTextAndSave(BOOK + '_corefed.txt', BOOK + '_corefed_fasttext.model', sg=1, hs=1, size=300, iter=15, window=12, negative=0)
```
- there will be two models: hp_corefed_text8.model and hp_corefed_fasttext.model
- put this models to config.py in https://github.com/gwohlgen/digitalhumanities_dataset_and_eval as described in this repo
- run 'python analogies_evaluation.py hp'  and 'python doesnt_match_evaluation.py hp' commands in your terminal
- there will be analogies and does not match results in terminal 
 


