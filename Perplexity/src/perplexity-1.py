import random
import os
import re
from decimal import *
os.chdir('..')
os.chdir('..')
parent=os.getcwd()


path1="Model/label1.1gram.lm"
path2="SplitData/train/label2.txt"
filename1=os.path.join(parent,path1)
filename2=os.path.join(parent,path2)
with open(filename1,'r',encoding='utf-8') as f: 
    text=f.readlines()



dict_val={}

for line in text:
    list_t= line.split("|") 
    word=list_t[0]
    value=list_t[1]
    dict_val[word]=value.replace('\n','')
    
with open(filename2,'r',encoding='utf-8') as f: 
    text2=f.read().split('\n')

new_text=[]

for i in range (0,len(text2)-2):

    new_text.append(text2[i])
   
num=1
for word in new_text:
    if word != "<s>" and word!= "</s>":
        if word in dict_val:
            num =num* Decimal(dict_val[word])



n=len(new_text)

x=-1/n
output= pow(num,Decimal(x))

print(output)