import csv
import queue 
from anytree import Node, RenderTree  
import os

cur_path = os.path.dirname(__file__)

#path for csv input and output 
csv_path= os.path.relpath('../in/Entries.csv', cur_path)
input_path= os.path.relpath('../in/in_1.txt', cur_path)
output_path= os.path.relpath('../out/out_1.txt', cur_path)

#this function converts persian alphabet to english according to the dictionary
def convert(fchar):  
    with open(csv_path, 'r') as _filehandler:
        csv_file_reader = csv.DictReader(_filehandler)
        for row in csv_file_reader:
            if( row['WrittenForm']== fchar):
                return row['PhonologicalForm']
            
#this function assembels a list into a string without space
def assemble(line):
    output_line=''.join(line)
    return output_line

#this function identifies wether this  PhonologicalForm exist or not  
def in_dict(word):
    with open(csv_path, 'r') as _filehandler:
        csv_file_reader = csv.DictReader(_filehandler)
        for row in csv_file_reader:
             if( row['PhonologicalForm']== word):
                return True
    return False

#this function returens the position of a node in string    
def pos_of_node(node):
    leng=0
    while(node.name !="root"):
        leng=leng+len(node.name)
        node=node.parent
    return leng    


#this function reads complete sentences from tree and returnes them in eng format
def read_sen(tree,level,line):
    all_sent=[]
    while(level>0):
        for node in tree[level]:
            sent=[]
            if(pos_of_node(node)>=len(line)):
                while(node.name !="root"):
                    sent.append(node.name)
                    node=node.parent
                all_sent.append(list(reversed(sent)))
        level=level-1
        
    return all_sent

#this function converts back english alphabet to persion
def convert_back(eng_list):
    all_farsi_sent=[]
    for sent in eng_list:
        farsi_sent=[]
        for word in sent:
            with open(csv_path, 'r') as _filehandler:
                csv_file_reader = csv.DictReader(_filehandler)
                for row in csv_file_reader:                    
                    if( row['PhonologicalForm']== word  ):
                        farsi_sent.append(row['WrittenForm'])
                        break
                        

        all_farsi_sent.append(farsi_sent)
        
    return all_farsi_sent


#reads line from input file
line_f=[]
f = open(input_path, "r")
for line in f:
    end=0
    first=0
    for char in line:
        end=end+1
        if(char== " "):
            line_f.append(convert(line[first:end-1]))
            first=end        
        if(end==len(line)):
            line_f.append(convert(line[first:end]))
      

  
line_f=assemble(line_f)


#constructing the tree
tree=[]
tree.append([])

#main loop - completing the tree
j=0
tree_row=0
tree[0].append(Node("root"))
while(True):     
    for node in tree[tree_row]:
        tree.append([])
        j=pos_of_node(node)
        for i in range (j+1,len(line_f)+1):
            if(in_dict(line_f[j:i])):
                tree[tree_row+1].append(Node(line_f[j:i],parent=node))
                
    
    tree_row=tree_row+1     
    if(len(tree[tree_row])==0):
        #printing the tree is commented below
        # for pre, fill, node in RenderTree(tree[0][0]):
        #     print("%s%s" % (pre, node.name))
        final_eng=read_sen(tree,tree_row-1,line_f)

        break   

    


farsi_final=convert_back(final_eng)

#some process on output and wirting on output file

file1 = open(output_path,"w") 
for sent in farsi_final:
    done="-".join(sent)
    file1.write(done)
    file1.write("\n") 
