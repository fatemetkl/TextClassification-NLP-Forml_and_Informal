# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#ham module for normalizing and tokenizing
from hazm import *
import os
import operator


normalizer = Normalizer()


stemmer = Stemmer()
lemmatizer = Lemmatizer()

new_words=[]
new_words2=[]
mycwd = os.getcwd()
os.chdir('..')
os.chdir('..')
parent=os.getcwd()
#reading data from data/label 1 , normalazing , tokenizing and stemming words then writing it into label1.txt
#lable1 
path1="Data/label1.txt"
filename=os.path.join(parent,path1)
with open(filename,'r',encoding='utf-8') as f:

        text = f.read()

        text=normalizer.normalize(text) 
        words = word_tokenize(text)
        for word in words:
                s=stemmer.stem(word)
                new_words.append(s)


filename1=os.path.join(parent,'ProcessedData/label1.txt')                
k = open(filename1,'w')
output=''
for item in new_words:
        output=output+item
        output=output+"\n"
k.write(output)
k.close()

#the sam esteps for label2
path2="Data/label2.txt"
filename=os.path.join(parent,path2)
with open(filename,'r',encoding='utf-8') as f:

        text = f.read()

        text=normalizer.normalize(text) 
        words = word_tokenize(text)
        for word in words:
                s=stemmer.stem(word)
                new_words2.append(s)


filename2=os.path.join(parent,'ProcessedData/label2.txt')                
k = open(filename2,'w')
output=''
for item in new_words2:
        output=output+item
        output=output+"\n"
k.write(output)
k.close()