import os
import random

train_dict_1={}#old
train_dict_2={}#new
num_1=0 #old
num_2=0#new
vocab_1=0
vocab_2=0
num_class_1=0
num_class_2=0
#new features are set to zero
f_has_=0
f_neshas=0

mycwd = os.getcwd()
os.chdir('..')
os.chdir('..')
parent=os.getcwd()
path1="train.txt"
path2="test.txt"
filename1=os.path.join(parent,path1)
filename2=os.path.join(parent,path2)
path3="Maxent/stopwords.txt"
filename3=os.path.join(parent,path3)
stoplist=''
#read stopwords
with open(filename3,'r',encoding='utf-8') as f:
    stoplist=f.read().split("\n")


with open(filename1,'r',encoding='utf-8') as f:
    train_data=f.read().split('\n')

data=[]
for entry in train_data:
    temp={}
    list_train=entry.split(" ")
    if list_train[0]=="OLD":
        sent="قدیمی"+" "
    if list_train[0]=="NEW":
        sent="جدید"+" "    
    for item in list_train[1:len(list_train)]:
        #checking this new feature
        f_has_=0
        f_neshas=0
        for char in item:
            if char=='_':
                f_has_=1
        if item=="نشس":
            f_neshas=1
        if item not in stoplist and item !='.' and item!=':':
            if item not in temp:
                temp[item]=1
            else:
                temp[item]+=1    
    for item in temp:
        sent+= str(item) +":" + str(temp[item])+ " "
    sent+="f_has_:"+ str(f_has_) +" "     # new feature for _   
    sent+="f_neshas:"+ str(f_neshas) +" " # new feature for verb neshas

    data.append(sent[0:len(sent)-1])    
path_dest='Maxent/input.train2.txt'
filename_train=os.path.join(parent,path_dest)
k = open(filename_train,'w',encoding='utf-8')
output=''
for item in data:
    k.write(item)
    k.write("\n")
k.close()                    

#test

with open(filename2,'r',encoding='utf-8') as f:
    train_data=f.read().split('\n')

data=[]
for entry in train_data:
    temp={}
    list_train=entry.split(" ")
    if list_train[0]=="OLD":
        sent="قدیمی"+" "
    if list_train[0]=="NEW":
        sent="جدید"+" "    
    for item in list_train[1:len(list_train)]:
        #checking _ feature in test
        f_has_=0
        for char in item:
            if char=='_':
                f_has_=1
        if item not in stoplist and item !='.' and item!=':':
            if item not in temp:
                temp[item]=1
            else:
                temp[item]+=1    
    for item in temp:
        sent+= str(item) +":" + str(temp[item])+ " "
    sent+="f_has_:"+ str(f_has_) +" "     # new feature for _   
    sent+="f_neshas:"+ str(f_neshas) +" " # new feature for verb neshas  
        
    data.append(sent[0:len(sent)-1])    
path_dest='Maxent/input.test2.txt'
filename_train=os.path.join(parent,path_dest)
k = open(filename_train,'w',encoding='utf-8')
output=''
for item in data:
    k.write(item)
    k.write("\n")    
k.close()      