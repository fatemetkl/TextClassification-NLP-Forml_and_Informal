import random
import os
import re
mycwd = os.getcwd()
os.chdir('..')
parent=os.getcwd()
path1="label1.txt"
path2="label2.txt"
filename=os.path.join(parent,path1)

with open(filename,'r',encoding='utf-8') as f:
    
    data1=f.read().replace('...',"</s>\n<s>")
    data1=data1.replace('?',"</s>\n<s>")
    data1=data1.replace('!',"</s>\n<s>") 
    data1=data1.replace('.',"</s>\n<s>")
    data1="<s>"+'\n' + data1                     
    data = data1.split('\n')        
          


test_size=int((len(data)*2)/10)
train_size=(len(data)*7)/10

first_index_test=random.randint(test_size,len(data)-test_size)



test_data = data[first_index_test:first_index_test+test_size]
train_data = data[0:first_index_test]+data[first_index_test+test_size:len(data)]


#write into test

filename_test=os.path.join(parent,'test/label1.txt')                
k = open(filename_test,'w')
output=''
for item in test_data:

        output=output+item
        output=output+"\n"
k.write(output)
k.close()


#write into train
filename_train=os.path.join(parent,'train/label1.txt')                
k = open(filename_train,'w')
output=''
for item in train_data:
        output=output+item
        output=output+"\n"
k.write(output)
k.close()




filename=os.path.join(parent,path2)

with open(filename,'r',encoding='utf-8') as f:
    
    data1=f.read().replace('...',"</s>\n<s>")
    data1=data1.replace('?',"</s>\n<s>")
    data1=data1.replace('!',"</s>\n<s>") 
    data1=data1.replace('.',"</s>\n<s>")
    data1="<s>"+'\n' + data1                     
    data = data1.split('\n')  

test_size=int((len(data)*2)/10)
train_size=(len(data)*7)/10

first_index_test=random.randint(test_size,len(data)-test_size)



test_data = data[first_index_test:first_index_test+test_size]
train_data = data[0:first_index_test]+data[first_index_test+test_size:len(data)]


#write into test

filename_test=os.path.join(parent,'test/label2.txt')                
k = open(filename_test,'w')
output=''
for item in test_data:
        output=output+item
        output=output+"\n"
k.write(output)
k.close()


#write into train
filename_train=os.path.join(parent,'train/label2.txt')                
l = open(filename_train,'w')
output=''
for item in train_data:
        output=output+item
        output=output+"\n"
l.write(output)
l.close()
