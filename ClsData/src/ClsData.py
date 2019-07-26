import os
import random

mycwd = os.getcwd()
os.chdir('..')
parent=os.getcwd()
path1="ProcessedData/label1.txt"
path2="ProcessedData/label2.txt"
filename1=os.path.join(parent,path1)
filename2=os.path.join(parent,path2)

with open(filename1,'r',encoding='utf-8') as f:
    data1=f.read().replace('\n',' ')
    data1=data1.replace('...',"...\n")
    data1=data1.replace('؟',"؟\n")
    data1=data1.replace('!',"!\n") 
    data1=data1.replace('.',".\n")                    

#adding OLD label to data

string_total_label1=''
for item in data1:
    if item=='\n':
        item="\nOLD"
    string_total_label1+= item
string_total_label1 = "OLD" + string_total_label1 
string_total_label1 =  string_total_label1[0:len(string_total_label1)-4]




with open(filename2,'r',encoding='utf-8') as f:
    data=f.read().replace('\n',' ')
    data=data.replace('...',"...\n")
    data=data.replace('؟',"؟\n")
    data=data.replace('!',"!\n") 
    data=data.replace('.',".\n")                    

#adding NEw lable to data
string_total_label2=''
for item in data:
    if item=='\n':
        item="\nNEW"
    string_total_label2+= item
string_total_label2 = "NEW" + string_total_label2
string_total_label2 =  string_total_label2[0:len(string_total_label2)-4]

total_data=string_total_label1+"\n"+string_total_label2

lines=[]
s=''
for item in total_data:
    if item!='\n':
        s+= item
    else:
        lines.append(s)
        s=''



#shuffle data

random.shuffle(lines) #shuffle method
test=[]
train=[]
# 80% of data is train and the rest of it is seprated as test
for i in range (0,int(len(lines)*0.8)):
    train.append(lines[i])
for i in range (int(len(lines)*0.8),len(lines)):
    test.append(lines[i])

#writing into files

filename_train=os.path.join(parent,'train.txt')                
k = open(filename_train,'w')
output=''
for line in train:
    output+=line+'\n'
k.write(output)
k.close()




filename_test=os.path.join(parent,'test.txt')                
k = open(filename_test,'w')
output=''
for line in test:
    output+=line+'\n'
k.write(output)
k.close()
