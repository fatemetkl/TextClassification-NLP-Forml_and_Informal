# TextGen
I have 3 programs for each n gram in srch
- 1) TextGen-1.py
seed : 70
- 2)TextGen-2.py
seed : 30
- 3)TextGen-3.py
label :50

first you need to enter seen and number of sentence
seed=input("Enter seed : ") 
n = input("Enter n : ") 

## uniagram
it will find a random length for each sentence
the first word is selected randomly
then find the greatest P in words ( checks not to be repeated)
after that , adds it t sentence
```
for i in range(0,int(n)):
    rand_word=random.choice(words)
    rand_size=random.randint(5,10)
    sentence=[]
    sentence.append(rand_word)
    for k in range (0,rand_size):
        max_t=0
        next_word=''
        for word in dict_val:
            if word not in sentence:
                if Decimal(dict_val[word])>Decimal(max_t):
                    max_t= dict_val[word]
                    next_word=word
        sentence.append(next_word)  
```
## biagram
first it randomly select 2 words (A B) from biagram, the first one should be <s> beginning of sentence
and it continues until it reaches </s>  when the second word in biagram in </s> it stops selecting
in each step it finds the best matching with greatest p from biagram
in which for example : (w1 w2 ) -> the next can be (w2 ?) , ? is whatever with more p
also it checks in order not to choose repeated ones

## trigram
it works almost the same unless it considers 2 situations:
for example
- 1) (w1 w2 w3 ) -> next one could be : (w2 w3 w4)

- 2)(w1 w2 w3 ) -> next one could be : (w3 w4 w5)

it should add at least one word


