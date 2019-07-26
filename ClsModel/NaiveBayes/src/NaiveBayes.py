import os
import random
import math

train_dict_1={}#old
train_dict_2={}#new
num_1=0 #old
num_2=0#new
freq_1={}
freq_2={}
vocab_1=0
vocab_2=0
num_class_1=0
num_class_2=0


mycwd = os.getcwd()
os.chdir('..')
os.chdir('..')
parent=os.getcwd()
path1="train.txt"
path2="test.txt"
filename1=os.path.join(parent,path1)
filename2=os.path.join(parent,path2)
path3="NaiveBayes/stopwords.txt"
filename3=os.path.join(parent,path3)
stoplist=''
#read stopwords
with open(filename3,'r',encoding='utf-8') as f:
    stoplist=f.read().split("\n")


with open(filename1,'r',encoding='utf-8') as f:
    train_data=f.read().split('\n')

for entry in train_data:
    list_train=entry.split(" ")
    if list_train[0]=="OLD":  #important : specify first class here
        num_class_1+=1
        for item in list_train[1:len(list_train)]:
            if item not in stoplist:
                num_1+=1
                if item not in train_dict_1:
                    train_dict_1[item]=1
                    vocab_1+=1
                else:
                    train_dict_1[item]+=1  

    elif list_train[0]=="NEW":
        num_class_2+=1
        for item in list_train[1:len(list_train)]:
             if item not in stoplist:
                num_2+=1
                if item not in train_dict_2:
                    train_dict_2[item]=1
                    vocab_2+=1
                else:
                    train_dict_2[item]+=1  

for item in train_dict_1:
        freq_1[item]=(train_dict_1[item]+1)/(num_1+vocab_1+1)
for item in train_dict_2:
        freq_2[item]=(train_dict_2[item]+1)/(num_2 +vocab_2+1)       

not_in_corpus_prob_1= 1/(num_1+vocab_1+1)
not_in_corpus_prob_2= 1/(num_2 +vocab_2+1)
prob_class1=num_class_1/(num_class_1+num_class_2)
prob_class2=num_class_2/(num_class_1+num_class_2)



with open(filename2,'r',encoding='utf-8') as f:
    test_data=f.read().split("\n")

out=[]
maximum=[]
for entry in test_data:
    prob_class_1=1
    prob_class_2=1
    list_test=entry.split(" ")
    for item in list_test[1:len(list_test)]:
        if item not in stoplist :
            if item in freq_1:
                prob_class_1= prob_class_1*freq_1[item]
            else :
                prob_class_1=prob_class_1*not_in_corpus_prob_1
            if item in freq_2:
                prob_class_2=prob_class_2*freq_2[item]
            else :
                prob_class_2=prob_class_2* not_in_corpus_prob_2  
    if prob_class_1 <=0 or prob_class_2<=0  :
        continue           
    out.append( "OLD" +" " + str(math.log10(prob_class_1*prob_class1)) +" "+"NEW"+" "+str(math.log10(prob_class_2*prob_class2)))
    if prob_class_1*prob_class1< prob_class_2*prob_class2:
        maximum.append("NEW")
    else:
        maximum.append("OLD")    
#save output model
path_dest='NaiveBayes/Test.output.txt'
filename_train=os.path.join(parent,path_dest)
k = open(filename_train,'w',encoding='utf-8')
output=''
for item in out:
    k.write(item)
    k.write("\n")    
k.close()                     
# calculate recall precision accuracy and F1
truePos=0
falsePos=0
trueNeg=0
falseNeg=0
class1="OLD"
class2="NEW"

for i in range (0,len(out)):
    if maximum[i]==class1 and test_data[i][0:3]==class1:
        truePos+=1
    elif maximum[i]==class1 and test_data[i][0:3]==class2:
        falsePos+=1
    elif maximum[i]==class2 and test_data[i][0:3]==class2:
        trueNeg+=1
    elif maximum[i]==class2 and test_data[i][0:3]==class1:    
        falseNeg+=1    

prec= truePos/(truePos+falsePos)
recall=truePos/(truePos+falseNeg)
F1=2* (prec*recall)/(prec+recall)
acc= (truePos+trueNeg)/ (trueNeg+truePos+falseNeg+falsePos)

out2=[str(prec),str(recall),str(F1),str(acc)]


path_dest='NaiveBayes/Test.report.txt'
filename_train=os.path.join(parent,path_dest)
k = open(filename_train,'w',encoding='utf-8')
output=''
for item in out2:
    k.write(item)
    k.write("\n")    
k.close()  
        
    
   
        