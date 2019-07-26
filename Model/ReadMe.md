# MODEL 

## first of all
I made a list of all the words in text named as text and a list of all vocabs in text named as vocab 
vocab contains an unk word 
"the" and some other words if is needed is removed from vocab list in order to be recognized ans 'unk'

## 1gram model
###### input 
```
def Model_1(text,vocab):
```
##### output
(result is the calculated p(w)=count(w)+1/(token + vocab+1) )
```
   for item in dictionay:
        result= (dictionay[item]+1)/(token+vocab_num+1)
        output += uniqe[i]+'|'+ str(result) + '\n'
        i+=1    
        
    return output
```
for unigram <s> and </s> is removed : we don't need them
dictionay[item] == number of each word in text
dictionary['unk] == number of out of vocab words such as 'the'in test

## 2gram model

##### input 
```
def Model_2(text,vocab):
```
here I have a bigram={} counting number of biagrams in text
here I check 4 states (having different combinations with 'unk') making different biagrams

1)(word word) both in vocab
```
     if text[i] in vocab and text[i-1] in vocab:
       both=pre +" "+ now
```
2)('unk' word ) first not in vocab

```
        elif text[i] in vocab and text[i-1] not in vocab:
            both= "unk" +" "+ now
```
3)(word 'unk') second not in vocab
```
        elif now not in vocab and pre in vocab:
            both= pre +" "+ "unk"
```
4) ('unk 'unk') both are unknown

```
        elif text[i] not in vocab and text[i-1] not in vocab:
            both= "unk" +" "+ "unk"
```
##### RESULT 
formula :
result= (bigram[item]+1)/(dictionay[word1] +vocab_num+1)
* bigram[item] = count of (w1,w2)
* dictionay[word1]= count of (w2)
return bigram,output 
- we need biagram for calculating trigram

## 3gram model


##### input 

```
def Model_3(text,vocab,bigram):
```

-in this function I fill trigram={}
-like above there are 7 pussible states considering 'unk'

- 1) 3 of them are known

```
      if pre_1 in vocab and pre_2 in vocab and now in vocab:
       both= pre_2 + " "+pre_1+ " " + now
```

- 2) in there three states one of them is 'unk' in different places

```
-    elif pre_1 in vocab and pre_2 in vocab and now not in vocab:
        both= pre_2 + " "+pre_1+ " " + "unk"


-        elif pre_1 in vocab and pre_2 not in vocab and now in vocab:            
            both= "unk"+ " "+pre_1+ " " + now

-         elif pre_1 not in vocab and pre_2 in vocab and now in vocab:
            both= pre_2+ " "+"unk"+ " " + now
```

- 3) tow of them are 'unk

```
-         elif pre_1 not in vocab and pre_2 not in vocab and now in vocab:
            both= "unk"+ " "+"unk"+ " " + now

-         elif pre_1 not in vocab and pre_2  in vocab and now not in vocab:
            both= pre_2+ " "+"unk"+ " " + "unk"

-         elif pre_1 not in vocab and pre_2  in vocab and now not in vocab:
            both= "unk+ " "+pre_2+ " " + "unk"

```
- all of them are unks
```
else:
            both= "unk" + " "+"unk"+ " " + "unk"
```

##### output
formula p(w1|w2w3): count of (w1,w2,w3)+1/ count (w1,w2)+vocab+1

```
        result= (trigram[item]+1)/(bigram[word1 + " "+word2] +vocab_num+1)
```

## result 
the given test was given to models and desired output was observed 
##### compaire
mine :
<s>|dogs|chase|0.3076923076923077
ref :
<s>|dogs|chase|0.3076



