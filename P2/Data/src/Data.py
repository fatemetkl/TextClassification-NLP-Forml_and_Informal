import os
import re
#specifing directories for storing
mycwd = os.getcwd()
os.chdir('..')
parent1=os.getcwd()
os.chdir('..')
parent=os.getcwd()
#reading and cleaning related to label1 (new books) then storing in label1.txt
label1="Data/label1.txt"
k = open(os.path.join(parent,label1),'w')
path1="RawData/gile.txt"
path2="RawData/yeki.txt"
path3="RawData/jalal.txt"
filename=[os.path.join(parent,path1),os.path.join(parent,path2),os.path.join(parent,path3)]
for name in filename:
    with open(name) as f:
        text = f.read()
    text=text.replace("_","")
    text=re.sub(r'([?!.])+',r"\1\n",text)
    text=re.sub(r'([( )])', ' ', text)
    text=text.replace('\n\n','\n')

    k.write(text)
k.close()


#reading and cleaning data related to label2 (old books) then storing it in label2.txt
label2="Data/label2.txt"
k = open(os.path.join(parent,label2),'w')
path4="RawData/1001.txt"
path5="RawData/kelile_demne.txt"
filename2=[os.path.join(parent,path4),os.path.join(parent,path5)]

for name in filename2:
    with open(name) as f:
        text = f.read()


    text=text.replace("_","")
    text=text.replace("|","")
    text=re.sub(r'([?!.])+',r"\1\n",text)
    text=re.sub(r'([( )])', ' ', text)
    text=text.replace('\n\n','\n')

    k.write(text)
k.close()