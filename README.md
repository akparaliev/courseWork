# courseWork
## milestone-one.py
### 3 functions:
#### preprocessFile(filePath, outputFilePath)
- filePath - path to your text(examples: hp.txt or asoif.txt)
- outputFilePath - where your preprocessed text will be saved
#### executeCoref(sentenceCount, targetTextPath, outputFilePath)
- sentenceCount - count of sentences that each paragraph has
- targetTextPath - path to your text(in task case - path to preprocessed text)
- outputFilePath - where your corefed text will be saved
#### trainModelAndSave(filePath, outputFilePath)
- filePath - path to your text(in task case - path to corefed text)
- outputFilePath - where your model will be saved, this file is in vec format

## run doesn't match or analogies script
- clone this repo: https://github.com/gwohlgen/digitalhumanities_dataset_and_eval/
- put model to models folder
- and scripts from src folder

## ERRORS:
- executing hp books txt with 1 or 4 sentences in paragraph is OK
- executing asoif books txt with 4 sentences causes MemoryError on of the internal scripts of spacy.
