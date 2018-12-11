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
- and run scripts from src folder

##  Results:
- results in folder 'results'
- w2v training settings: cbow_mean=0, min_count=5, size=300, window=5, negative=0, hs=1, sample=0.001, workers=12
