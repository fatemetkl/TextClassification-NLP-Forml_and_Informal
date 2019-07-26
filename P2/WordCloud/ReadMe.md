# WordCloud
There are two src codes used here:
> WordCloud.py and stopword.py 

the first one created 4 wordclouds from all of the words bud the second one (stopword.py)
omits stopwords used in farsi.

modules used :
>from wordcloud import WordCloud

>import arabic_reshaper

for farsi word shape

>from bidi.algorithm import get_display

I calculated these dictionaries for each word:

> newwords={} #dict of words in label1 (word,num)

> oldwords={} #dict of words in label2 (word,num)

> token=0 #total token number

> freqnew={} #dict of label1 freq

frequencies / token num (all the words)

> freqold={}#dict of label2 freq 

> freqNewsubOld={}
new (label 1) - old (label 2) *100000

if word was i the first one and the second label as well clculate :

freqNewsubOld[word] = int ((freqnew[word] - freqold[word])*100000)

otherwise, just use label1 freq : freqNewsubOld[word] = int (freqnew[word]  *100000)

> freqOldsubNew={}

the same approach as above is used here

old (label2) - new (lable 1) *100000

# stopword
for the rest of the coluds the only difference is that befor adding a word it is checked for 
not being in stopwords list
> if word not in StopWords:

# RESULT EXOLANATION
as it is shown in wordclouds befor omitting stop word label1 and label2 (new and old books) are full of
words that are not important like ",از خود که

and all the stop words

for image 3 is the same 
image 4 shows more old words which indicates that there are specific old words used.

considering that stop words are removed from data in rest of the wordClouds they represent data better.

image 5 :ول  کار شب خانه اتاق سر مرد حرف

these words are used mostly these days in social stories

image 6: شب روز کار همسر پدر سر کن حال سفر خانه شهر

these words are mostly used in past (some of theme are being used these days as well)

image 7: افسوس زندگی بده یاری پول

these word are just being used frequently these years

image 8: جادوگر پادشاه دلیر بیگانه شهره

at the end , these words don't apply to the modern way of speaking in farsi