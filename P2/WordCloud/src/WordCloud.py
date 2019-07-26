# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import operator
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display


#new = label 1
# old =label 2
mycwd = os.getcwd()
os.chdir('..')
os.chdir('..')
parent=os.getcwd()

newwords={} #dict of words in label1 (word,num)
oldwords={} #dict of words in label2 (word,num)
StopWords={}
token=0 #total token number
freqnew={} #dict of label1 freq
freqold={}#dict of label2 freq
textold=""
textnew=""
textNewsubOld=""
textOldsubNew=""

#lable1 
# counting word freq and text for both labels
path1="ProcessedData/label1.txt"
filename=os.path.join(parent,path1)
with open(filename,'r',encoding='utf-8') as f:
    text=f.readlines()
    for word in text:
        #count tokens
        token +=1
        #text for label1
        textnew += ' ' + word 
        if word in newwords:
            newwords[word] +=1
        else:
            newwords[word]=1    

#lable2
path2="ProcessedData/label2.txt"
filename2=os.path.join(parent,path2)
with open(filename2,'r',encoding='utf-8') as f:
    text=f.readlines()
    for word in text:
        #count tokens
        token +=1
        textold += ' ' + word  #text for label2
        if word in oldwords:
            oldwords[word] +=1
        else:
            oldwords[word]=1    

#frequencies / token num (all the words)
    
for item in newwords:
    freqnew[item] = newwords[item]/token

for item in oldwords:
    freqold[item] = oldwords[item]/token   



#diff freq
freqNewsubOld={}
#new (label 1) - old (label 2) *100000
#if word was i the first one and the second label as well clculate freqNewsubOld[word] = int ((freqnew[word] - freqold[word])*100000)
#otherwise, just use label1 freq : freqNewsubOld[word] = int (freqnew[word]  *100000)
for word in freqnew:
    if word in freqold:  
        if(freqnew[word]>freqold[word]):
            freqNewsubOld[word] = int ((freqnew[word] - freqold[word])*100000)
    else:
        freqNewsubOld[word] = int (freqnew[word]  *100000)   
 #text for label1 - label2   
for item in freqNewsubOld:
    textNewsubOld += (' ' + item ) * freqNewsubOld[word]
    
# the same approach as above is used here
# old (label2) - new (lable 1) *100000
freqOldsubNew={}
for word in freqold:
    if word in freqnew:
        if(freqold[word]>freqnew[word]):
            freqOldsubNew[word] = int((freqold[word] - freqnew[word])*100000)
    else:
        freqOldsubNew[word] = int(freqold[word]*100000)    
    
# text for label2 - label 1
for item in freqOldsubNew:
    textOldsubNew += (' ' + item) * freqOldsubNew[word]


#creating clouds
textnew=arabic_reshaper.reshape(textnew)
textnew=get_display(textnew)
textold=arabic_reshaper.reshape(textold)
textold=get_display(textold)
textNewsubOld=arabic_reshaper.reshape(textNewsubOld)
textNewsubOld=get_display(textNewsubOld)
textOldsubNew=arabic_reshaper.reshape(textOldsubNew)
textOldsubNew =get_display(textOldsubNew)

#displaying clouds

WordCloudnew = WordCloud(font_path='WordCloud/src/BNazanin.ttf', background_color='white', height=2000, width=2000)
WordCloudnew.generate(textnew)
plt.imshow(WordCloudnew)
plt.axis("off")
plt.title('new')
plt.show()

WordCloudold = WordCloud(font_path='WordCloud/src/BNazanin.ttf', background_color='white', height=2000, width=2000)
WordCloudold.generate(textold)
plt.imshow(WordCloudold)
plt.axis("off")
plt.title('old')
plt.show()


WordCloudnewsubold = WordCloud(font_path='WordCloud/src/BNazanin.ttf', background_color='white', height=2000, width=2000)
WordCloudnewsubold.generate(textNewsubOld)
plt.imshow(WordCloudnewsubold )
plt.axis("off")
plt.title('newSubold')
plt.show()

WordCloudoldSubnew = WordCloud(font_path='WordCloud/src/BNazanin.ttf', background_color='white', height=2000, width=2000)
WordCloudoldSubnew.generate(textOldsubNew)
plt.imshow(WordCloudoldSubnew )
plt.axis("off")
plt.title('oldSubnew')
plt.show()