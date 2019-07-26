import random
import os
import re
from decimal import *
os.chdir('..')
os.chdir('..')
parent=os.getcwd()


path1="Model/label2.3gram.lm"
path2="SplitData/train/label2.txt"
filename1=os.path.join(parent,path1)
filename2=os.path.join(parent,path2)
with open(filename1,'r',encoding='utf-8') as f: 
    text=f.readlines()



dict_val={}

for line in text:
    list_t= line.split("|") 
    word1=list_t[0]
    word2=list_t[1]
    word3=list_t[2]
    value=list_t[3]
    dict_val[word1+" "+word2+" "+ word3]=value.replace('\n','')
    
with open(filename2,'r',encoding='utf-8') as f: 
    text2=f.read().split('\n')

new_text=[]

for i in range (0,len(text2)-2):

    new_text.append(text2[i])
        
num=1
for i in range(2,len(new_text)-1):
    word=new_text[i-2]+" "+new_text[i-1] +" "+ new_text[i]
    if word in dict_val:
        num =num* Decimal(dict_val[word])

n=len(new_text)
x=-1/n
output= pow(num,Decimal(x))

print(output)