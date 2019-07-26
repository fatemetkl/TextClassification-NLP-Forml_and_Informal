# comparing both ways

## result from naive bayes
- on test set:
precision : 0.8784722222222222
recall : 0.7485207100591716
F1 : 0.8083067092651758
acuuracy : 0.6977329974811083

## results from maxent (model.bin) 
* features are just count of words in each sentence :
From test.report.txt :
```
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data precision(قدیمی) = 0.9758119658119658
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data precision(جدید) = 0.9683333333333334
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data recall(قدیمی) = 0.9971348973607038
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data recall(جدید) = 0.8131034482758621
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data F1(قدیمی) = 0.9997687861271676
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data F1(جدید) = 0.9179245283018867
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data accuracy = 0.9849122807017544
```
### results from maxent with new features (model2.bin)
* more features are added :
from test.report2.txt
```
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data precision(قدیمی) = 0.9795678136890321
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data precision(جدید) = 0.9719363373553331
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data recall(قدیمی) = 0.99823248367367098
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data recall(جدید) = 0.8231054492732627
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data F1(قدیمی) = 0.9991212168201071
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data F1(جدید) = 0.9259645182013849
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data accuracy = 0.9897834447011294

``` 

- `precision` for maxent is more
- `recall` is more as well !
- `F1` for maxent is more
- `total accuracy` is far better
 as it is shown in result maxent has act better and has chosen good weights for words and features
- maxent is more complicated 

there are a lot of reasons for naive bayes to be weaker which I mentioned in Naive Bayes read me as well:

# 5.2 result analysis for Naive bayes
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


# RESULT analysis for maxent
# MaxEnt Features

first of all features were count of every word in a sentence
word(feature) : count (value)

sth like as input 205 :

 `جدید وزیر:1 چهره:1 پردرد:1 غمناک:1 خانه:1 آمد:2 سکو:1 سرا:1 نشس:1 سر:2 م:1 دو:1 دس:1 گرف:1 ،:1 دانه:1 اشک:1 دا:1 می‌ریخ:1 دختر:1 بالا:1`

`جدید` is the class2
in fact what we have chosen here as feature are tokens in each instance
and maxEnt gives weights for these words specifying their importance in chooseing between classes

* the sentence above is classified as class 2 (قدیمی) which is wrong
`array:204	قدیمی	0.8891237900187383	جدید	0.11087620998126164`

it shows that maybe we should define more features!

because the word `خانه` has appeared  lot in old texts

## choosing features

I sorted the list of the words in each class according to their count(word)
- it sounds like words containing `_‍` have appeared more in new text.
```
f_has_=0
        for char in item:
            if char=='_':
                f_has_=1
```
* f_has_=0(old) or f_has_=1(new)

- another feature can be the word `نشس` that appear in new texts while in old texts it is more like `نشسته`

```
f_neshas=0
        if item=="نشس":
            f_neshas=1

```

- adding thsese features to input
```
    sent+="f_has_:"+ str(f_has_) +" "     # new feature for _   
    sent+="f_neshas:"+ str(f_neshas) +" " # new feature for verb neshas
```
# RUNNING with new features and RESULT (maxent)

* all the new files for these new features are saved as .....2.txt for example : for previous model it was model.bin and this new one is model2.bin

it git a little bit better but because accuracy was reall good in the first place, it didnt change so much.

#### most frequent words of each class 
* these led to better feature choosing

 

