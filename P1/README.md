# HW1

In this homework, I tried to find different ways of saying a same sentence
which may cause ambiguity in it's meaning


### Prerequisites

I have used anytree module in python for my tree data structure
Installation:
```
pip install anytree
```

## Running and testing

RUN :
in src folder

```
python 1.py
```

input file path:
file must be in 'in' folder
its name should be specified in code
```

input_path= os.path.relpath('../in/in_1.txt', cur_path)
```
output file path:
```

input_path= os.path.relpath('../in/in_1.txt', cur_path)
```
csv file path:
```

csv_path= os.path.relpath('../in/Entries.csv', cur_path)
```


### code explanation 
My way for solving this :

I assumed each sentence in persin as a single string consisting of english chars without spaces between words.
Then started from the first char , finding all words that are in dictionary from that first char
These words constructed the first level of a tree with 'root' as root.
Afterwards, for each of these nodes in the first level, did the same thing considering the rest of the string from that point.
this process created a tree in which possibile way of spelling are ended with the last word of sentence and 
the ones that dosent mean any thing after a while wont endup in a complete sentence.
for example this is the cunstructed tree for the first test:
```

root
├── be
│   └── dun
└── bedune
    └── rang
        ├── 'A
        │   └── se
        │       ├── mA
        │       └── mAn
        │           ├── ze
        │           └── zeSt
        │               └── 'ast
        ├── 'As
        ├── 'Ase
        │   ├── mA
        │   └── mAn
        │       ├── ze
        │       └── zeSt
        │           └── 'ast
        └── 'AsemAn
            ├── ze
            └── zeSt
                └── 'ast


```
As shown above, only three leaves have ended in a complete sentence, therefore, there are only 3 alternatives .
