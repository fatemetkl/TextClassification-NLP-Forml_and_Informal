# Splitting data
what I did in this step is as follow:

### creating random partitions:
after defining the size of train and test
I made a random number that shows the place of test partition in data

```

test_size=int((len(data)*2)/10)
train_size=(len(data)*7)/10

first_index_test=random.randint(test_size,len(data)-test_size) 

test_data = data[first_index_test:first_index_test+test_size]
train_data = data[0:first_index_test]+data[first_index_test+test_size:len(data)]
```
besides I did some extra data processing to show start and end of the lines

```
    data1=f.read().replace('...',"</s>\n<s>")
    data1=data1.replace('?',"</s>\n<s>")
    data1=data1.replace('!',"</s>\n<s>") 
    data1=data1.replace('.',"</s>\n<s>")
    data1="<s>"+'\n' + data1                     
    data = data1.split('\n')
```

‍‍