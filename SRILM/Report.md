# SRLILM
### what I did!
first of all, get vocab list out of data with a program in src file
* vocav_1.txt (label1 ) and vocab_2.txt (label2)
then using these commands I got the count for both labels and after that 1gram 2gram and 3gram for label1 and 2 in a model file
```
sudo ./ngram-count -vocab vocab_1.txt -text label1.txt -order 3 -write count.txt -unk
```
resulted in :
* count1.txt and count2.txt

```
sudo ./ngram-count -vocab vocab_1.txt -read count1.txt -order 3 -lm label1.ngram.lm -gt1min 3 -gt1max 7 - gt2min 3 - gt2max 7 -gt3min 3 - gt3max 7
``` 
* output : label1.ngram.txt and label2.ngram.txt
  
# Perplexity with SRILM

* as the model for each data is consisted of 1gram , 2gram and 3gram for all of them we srilm gives one perplexity on each given input text

## label1 model

### train
```

file label1.txt: 1676 sentences, 32361 words, 15676 OOVs
0 zeroprobs, logprob= -30706.63 ppl= 47.03088 ppl1= 69.24256
```
### test
```
file label1_test.txt: 187 sentences, 3276 words, 1737 OOVs
0 zeroprobs, logprob= -3331.341 ppl= 85.1321 ppl1= 146.0879
```

## label2 model

### train
```
file label2.txt: 627 sentences, 17419 words, 9754 OOVs
‍‍0 zeroprobs, logprob= -11635.59 ppl= 25.30642 ppl1= 32.96215
‍‍‍‍‍```


### test
```
file label2_test.txt: 149 sentences, 5196 words, 2206 OOVs
0 zeroprobs, logprob= -6771.911 ppl= 143.6635 ppl1= 184.0149
```
#### putting it together

| train data    | test data     |model(1-2-3)grams|
| ------------- | ------------- |---------------- |
| 47.03088      | 85.1321       |label 1 model	  |
| 25.30642      | 143.6635      |label2 model	  |

### compairing with my own pp

| (1-2-3)grams  | 1gram      |   2gram    |   3gram |  data   | 
| ------------- | -----------|------------|---------|---------|
| 47.03088      | 34.522997  |3.3103759   |1.123527 | train 1 | 	   
| 85.1321       | 30.27922   |2.789710	  |1.099371 | test 1  |
| 25.3064       | 68.74472   |20.45919	  |24.8003  | train 2 |	   
| 43.6635       | 53.902124  |4.3535998	  |1.38775  | test 2  |

as it is shown as the n in ngram increases the perplexity increases as well. 
the result from srilm is roughly near the average of other 3 grams that I calculated.
in overall pp is more in test data compairing to train
 






