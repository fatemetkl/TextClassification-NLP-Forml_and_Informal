import random
import os
from decimal import *
os.chdir('..')
os.chdir('..')
parent=os.getcwd()


path1="Model/label1.1gram.lm"
filename1=os.path.join(parent,path1)
with open(filename1,'r',encoding='utf-8') as f: 
    text=f.read().split('\n')
dict_val={}
words=[]
new_text=[]

for i in range (0,len(text)-2):

    new_text.append(text[i])

for line in new_text:
    list_t= line.split("|") 
    word=list_t[0]
    value=list_t[1]
    dict_val[word]=value.replace('\n','')
    words.append(word)


seed=input("Enter seed : ") 
random.seed( int(seed) ) 
n = input("Enter n : ")  
output=""
for i in range(0,int(n)):
    rand_word=random.choice(words)
    rand_size=random.randint(5,10)
    sentence=[]
    sentence.append(rand_word)
    for k in range (0,rand_size):
        max_t=0
        next_word=''
        for word in dict_val:
            if word not in sentence:
                if Decimal(dict_val[word])>Decimal(max_t):
                    max_t= dict_val[word]
                    next_word=word
        sentence.append(next_word)        
    out_text=''
    for word in sentence:
        out_text+= word+" "
    output += out_text +'\n'




out_t=os.path.join(parent,'‫‪TextGen/label1.1gram.gen')                
f = open(out_t,'w')
f.write(output)
f.close()
