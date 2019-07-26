# perplexity
I have three files 
- 1)perplexity-1.py : for unigram
- 2)perplexity-2.py: for biagram
- 3)perplexity-3.py :for trigram


## unigram:
- after extracting words from text
- I calculated P(w) according to model unigram
- output is from pp formula 
```
num=1
for word in new_text:
    if word != "<s>" and word!= "</s>":
        if word in dict_val:
            num =num* Decimal(dict_val[word])

```
- dict_val = the amount of p(w) from model

then :

```
n=len(new_text)
x=-1/n
output= pow(num,Decimal(x))
```

## biagram
is the same as abouve except for calculatin P for biagram form the given biagram
```
for i in range(1,len(new_text)-1):
    word=new_text[i-1] +" "+ new_text[i]
    if word in dict_val:
        num =num* Decimal(dict_val[word])

n=len(new_text)
x=-1/n
output= pow(num,Decimal(x))
```

## trigram

same as above
```
num=1
for i in range(2,len(new_text)-1):
    word=new_text[i-2]+" "+new_text[i-1] +" "+ new_text[i]
    if word in dict_val:
        num =num* Decimal(dict_val[word])

n=len(new_text)
x=-1/n
output= pow(num,Decimal(x))
```
