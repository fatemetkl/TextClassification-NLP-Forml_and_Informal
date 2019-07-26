import random
import os
from decimal import *
os.getcwd()
os.chdir('..')
os.chdir('..')
parent=os.getcwd()


#seed = 15

path1="Model/label2.2gram.lm"
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
    word1=list_t[0]
    word2=list_t[1]
    value=list_t[2]
    if  len(value)>0:
        if value[0]=='0':
            dict_val[word1+" "+word2]=value.replace('\n','')
    if word1=="<s>":
        words.append(word1+" "+word2)    

seed=input("Enter seed : ") 
random.seed( int(seed) ) 
n = input("Enter n : ")  
output=''
for i in range(0,int(n)):
    rand_word=random.choice(words)
    word=rand_word.split(" ")[1]
    sentence=[]
    sentence.append(rand_word)
    while word!= "</s>":
        max_tt=0
        next_word=""
        for toupels in dict_val:
            pre=toupels.split(" ")[0]
            now=toupels.split(" ")[1]
            if word == pre and now not in sentence :
                if Decimal(dict_val[toupels]) > Decimal(max_tt):
                    max_tt=dict_val[toupels]
                    next_word=now
        word=next_word            
        sentence.append(next_word)
    out_text=''
    for word in sentence:
        out_text+= word+" "
    output += out_text +'\n'




out_t=os.path.join(parent,'‫‪TextGen/label2.2gram.gen')                
f = open(out_t,'w')
f.write(output)
f.close()


