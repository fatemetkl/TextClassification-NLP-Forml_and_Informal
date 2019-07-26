
import os

mycwd = os.getcwd()
os.chdir('..')
os.chdir('..')
os.chdir('..')
parent=os.getcwd()
path1="SplitData/train/label2.txt"
filename=os.path.join(parent,path1)

with open(filename,'r',encoding='utf-8') as f:
    corpus = f.read()
    corpus = corpus.split()
    vocal = []
    for word in corpus:
        if word not in vocal:
            vocal.append(word)
    vocal.sort() # sorts normally by alphabetical order
    vocal.sort(key=len, reverse=False) # sorts by descending length
with open('SRILM/Model/vocab_2.txt', 'w') as f:
    for word in vocal:
        f.write(word + '\n')
