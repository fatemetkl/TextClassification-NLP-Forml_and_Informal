# NaiveBayes

first of all , counted each token in each class and saved them into dictionaries:

- train_dict_1={}#old
- train_dict_2={}#new

meanwhile, I counted token num and vocab num in each class
after that, I calculated freq for each vocab and saved them in:
- freq_1={}
- freq_2={}

I used the below formula for P(class=c):
```
prob_class1=num_class_1/(num_class_1+num_class_2)
prob_class2=num_class_2/(num_class_1+num_class_2)

num_class= count of sentences
```
then I calculated prob for each word in class P(w|c)
and by multiplying prob of words in each sentence, P(sentence|class) was calculated
after that,it was multiplied by the prob of class
```
for class1:
math.log10(prob_class_1*prob_class1) 
```
# calculating recall precision accuracy and F1
 from the model above , prediction could be compaired with labels which are saved in test file
- for calculating tp,fn and... I used the below tabel

|  actual\Prediction-> | class 2 =NEW   | class 1 =OLD  |
| :---         |     :---:      |          ---: |
| class 2 =NEW | TN             | FP            |
| class 1 =OLD | FN             | TP            |

and the rest of it is saving into files and formulas


# 5.2 result analysis
one of the main problems with Naive bayes is that it dosent really care about the sequence of words in a sentence
it pays attention only to the words , using bag of words. In another hand it is so fast in training and testing

* now we can analys these situations:
#### 1)instance of true prediction class1 (OLD)

```
    if maximum[i]==class1 and test_data[i][0:3]==class1:
        truePos+=1
```
OLD رفیق نیز همین را گف و وقت آن خواستند بروند من رو به او گف : باید واقعه جالب اتفاق افتاده_باشد .

#### 2)if pediciton is class1(old) but true label is class2(new)
```
    elif maximum[i]==class1 and test_data[i][0:3]==class2:
        falsePos+=1
```
NEW و آن داس چنین اس که پدر ما ، مرد بود وارسته و کاسب که کالا از پیله ور و تجار می‌خرید و با سود اندک به مرد می‌فروخ ، که بین کالا گوناگون ، به عطر و پارچه علاقه یشتر داشت.

#### 3)if pediciton is class2 and true label is class2 (NEW)

```
    elif maximum[i]==class2 and test_data[i][0:3]==class2:
        trueNeg+=1

```
NEW و من غافل ، حت تصور این بود که همسر بعد از پنجاه سال ، رمز و راز جادو‌گر را ه از یاد برده_اس 

#### 4)if pediciton is class2(new) and true label is class1(old) 

```
    elif maximum[i]==class2 and test_data[i][0:3]==class1:    
        falseNeg+=1
```

NEW شهر باز پاسخ داد : من ه که پس از سال دور موفق به دیدار شده ، امید دا تو را خند و شاد ببین ، نه غمگین و افسرده .

- in the second and last cases predictions were wrong and one of the reasons is the iportance of words which are next to each other
- and another reason is the words themselves
- in the `second one` words like `داس` and `وارسته` seems to happen more in old stories, not in new ones, therefore our cassifire made mistake, we could make the same mistake too because of these words.
-  likewise in the last item there are words like `شاد` and`خنده` (these words have changed a little due to tokenization and lemmatization) mostly have appeared in new stories.
 
- Therefore in this cases the effect of `bag-of-word` is obvious.

- Another thing is the `sequence` in which words come aftre each other for example:
- in `second` item : the word `وارسته` is likely to happen in old texts but the phrase `وارسته و کاسب` may rarely happen in old books ,
- so this 2words after each other won't have big prob in old stories.
#### Q) in cases which prob for both classes is near which one and why has been chosen?
for example sentence 279:
```
OLD زن ب بدل را از من می‌گیر و این ه کار امشب که می‌خواه اشک مرا خون کن و می‌رو دخ مرد را دوباره ناخو می‌کن راست که دیگر شور را در آورد بله .
OLD -67.84175860449191 NEW -67.73375353695661

```
both are so close and OLD is chosen and it is chosen correctly. the reason for that is words like `خون` and `اشک` or `شور‍‍` . 
these words are confusing for humans too.
the reason for choosing it is only the bigger probability according to the probability of words 



