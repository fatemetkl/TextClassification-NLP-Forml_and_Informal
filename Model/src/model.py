import random
import os
import re


def Model_1(text,vocab):
    output=''
    dictionay={}
    vocab_num=0
    token=0
    uniqe=[]
    for w in text:
        if w != "<s>" and w!= "</s>":
            token +=1
            if w in vocab:
                if w in dictionay:
                    dictionay[w]+=1
                else:
                    uniqe.append(w)
                    vocab_num+=1
                    dictionay[w]=1  
            else:
                if "unk" in dictionay:
                    dictionay["unk"] +=1
                else:
                    dictionay["unk"]=1
                    uniqe.append("unk")
                    vocab_num+=1
               
    i=0
    for item in dictionay:
        result= (dictionay[item]+1)/(token+vocab_num+1)
        output += uniqe[i]+'|'+ str(result) + '\n'
        i+=1    
        
    return output   



def Model_2(text,vocab):
    dictionay={}
    vocab_num=0
    uniqe=[]
    for w in text:
        if w in vocab:
            if w in dictionay:
                dictionay[w]+=1
            else:
                uniqe.append(w)
                vocab_num+=1
                dictionay[w]=1  
        else:
            if "unk" in dictionay:
                dictionay["unk"] +=1
            else:
                dictionay["unk"]=1
                uniqe.append("unk")
                vocab_num+=1
#part2        
    
    bigram={}
    output=''
    for i in range(1,len(text)):
        pre=text[i-1]
        now=text[i]
        if pre=="</s>":
            continue
        
        if text[i] in vocab and text[i-1] in vocab:
            both=pre +" "+ now
            if both in bigram:
                bigram[both]+=1
            else:
                bigram[both]=1 

        elif text[i] in vocab and text[i-1] not in vocab:
            both= "unk" +" "+ now
            if both in bigram:
                bigram[both]+=1
            else:
                bigram[both]=1 
        elif now not in vocab and pre in vocab:
            both= pre +" "+ "unk"
            if both in bigram:
                bigram[both]+=1
            else:
                bigram[both]=1        
        elif text[i] not in vocab and text[i-1] not in vocab:
            both= "unk" +" "+ "unk"
            if both in bigram:
                bigram[both]+=1
            else:
                bigram[both]=1 
                    
    i=0
    vocab_num=vocab_num-2         
    for item in bigram:
        word1=item.split(" ")[0]
        word2=item.split(" ")[1]
        result= (bigram[item]+1)/(dictionay[word1] +vocab_num+1)
        output += word1 +'|'+ word2 +"|"+ str(result) +'\n'
        i+=1    

    return bigram,output   
                 
def Model_3(text,vocab,bigram):
    dictionay={}
    vocab_num=0
    uniqe=[]
    for w in text:
        if w in vocab:
            if w in dictionay:
                dictionay[w]+=1
            else:
                uniqe.append(w)
                vocab_num+=1
                dictionay[w]=1  
        else:
            if "unk" in dictionay:
                dictionay["unk"] +=1
            else:
                dictionay["unk"]=1
                uniqe.append("unk")
                vocab_num+=1
    trigram={}
    output=""
    for i in range(2,len(text)):
        pre_1=text[i-1]
        pre_2=text[i-2]
        now=text[i]
        if pre_1=="</s>":
            continue
        if pre_2 == "</s>":
            continue
        if pre_1 in vocab and pre_2 in vocab and now in vocab:
            both= pre_2 + " "+pre_1+ " " + now
            if both in trigram:
               trigram[both]+=1
            else:
                trigram[both]=1 
        elif pre_1 in vocab and pre_2 in vocab and now not in vocab:
            both= pre_2 + " "+pre_1+ " " + "unk"
            if both in trigram:
                trigram[both]+=1
            else:
                trigram[both]=1 
        elif pre_1 in vocab and pre_2 not in vocab and now in vocab:            
            both= "unk"+ " "+pre_1+ " " + now
            if both in trigram:
                trigram[both]+=1
            else:
                trigram[both]=1 
        elif pre_1 not in vocab and pre_2 in vocab and now in vocab:
            both= pre_2+ " "+"unk"+ " " + now
            if both in trigram:
                trigram[both]+=1
            else:
                trigram[both]=1 
        elif pre_1 not in vocab and pre_2 not in vocab and now in vocab:
            both= "unk"+ " "+"unk"+ " " + now
            if both in trigram:
                trigram[both]+=1
            else:
                trigram[both]=1 
        elif pre_1 not in vocab and pre_2  in vocab and now not in vocab:
            both= pre_2+ " "+"unk"+ " " + "unk"
            if both in trigram:
                trigram[both]+=1
            else:
                trigram[both]=1         
        else:
            both= "unk" + " "+"unk"+ " " + "unk"
            if both in bigram:
                bigram[both]+=1
            else:
                bigram[both]=1 
    vocab_num=vocab_num-2  
    i=0                    
    for item in trigram:
        word1=item.split(" ")[0]
        word2=item.split(" ")[1]
        word3=item.split(" ")[2]
        result= (trigram[item]+1)/(bigram[word1 + " "+word2] +vocab_num+1)
        output += word1 +'|'+ word2 +"|"+ word3 +"|"+ str(result) +'\n'
        i+=1    

    return output  
        
        






mycwd = os.getcwd()
os.chdir('..')
os.chdir('..')
parent=os.getcwd()


path1="SplitData/train/label1.txt"
path2="SplitData/train/label2.txt"
path3="Model/test/in.3gram"

filename1=os.path.join(parent,path1)
filename2=os.path.join(parent,path2)
# filename3=os.path.join(parent,path3)

text=''
list_1=[]
with open(filename1,'r',encoding='utf-8') as f: 
    text=f.readlines()


for word in text:
    word=word.replace("\n","")
    list_1.append(word)

vocab=[]
for i in range (0,len(list_1)-1):
    if(list_1[i]!= "the" ):
        vocab.append(list_1[i])



output_1_label1=Model_1(list_1,vocab)

# write into Model\label1.1gram.lm
label1_1gram=os.path.join(parent,'Model/label1.1gram.lm')                
k = open(label1_1gram,'w')
k.write(output_1_label1)
k.close()



bigram,output_2_label1 =Model_2(list_1,vocab)

# write into Model\label1.2gram.lm
label1_2gram=os.path.join(parent,'Model/label1.2gram.lm')                
k = open(label1_2gram,'w')
k.write(output_2_label1)
k.close()


output_3_label1=Model_3(list_1,vocab,bigram)

path_rigram=os.path.join(parent,'Model/label1.3gram.lm')                
k = open(path_rigram,'w')
k.write(output_3_label1)
k.close()



#label2
text=''
list_1=[]
with open(filename2,'r',encoding='utf-8') as f: 
    text=f.readlines()


for word in text:
    word=word.replace("\n","")
    list_1.append(word)

vocab=[]
for i in range (0,len(list_1)-1):
    if(list_1[i]!= "the" ):
        vocab.append(list_1[i])


        


output_1_label1=Model_1(list_1,vocab)

# write into Model\label1.1gram.lm
label1_1gram=os.path.join(parent,'Model/label2.1gram.lm')                
k = open(label1_1gram,'w')
k.write(output_1_label1)
k.close()



bigram,output_2_label1 =Model_2(list_1,vocab)

#write into Model\label1.2gram.lm
label1_2gram=os.path.join(parent,'Model/label2.2gram.lm')                
k = open(label1_2gram,'w')
k.write(output_2_label1)
k.close()

output_3_label1=Model_3(list_1,vocab,bigram)

path_rigram=os.path.join(parent,'Model/label2.3gram.lm')                
k = open(path_rigram,'w')
k.write(output_3_label1)
k.close()

