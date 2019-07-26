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
- it sounds like words containing `_‍` have appeared more in new text ( 2 part verbs = longer verbs).
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
######**note: I added more features such as `biagram`, but results  approximately remained the same , so more features were not neseccary

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
for class2 (new) :
م 33
بچه 34
نگاه 35
پایین 35
مرا 35
`کرده_بود 36`
ا 36
حالا 36
هیچ 37
زمین 37
زد 37
حاج 37
اتاق 38
شما 38
لب 38
زیر 38
رف 38
دست 39
روز 39
آمد 39
`شده_بود 39`
پیدا 39
خیل 39
فکر 39
یا 41
دور 41
دل 41
هنوز 41
حال 42
بالا 42
افتاد 43
همه 44
حرف 44
گو 44
خوب 45
بعد 45
طرف 46
کرده 46
همین 46
جا 46
چند 47
دید 48
طور 48
نبود 49
`می‌شد 49`
آب 49
راه 49
گیله 49
کن 50
بلند 50
کس 52
شب 52
اگر 52
داد 53
کند 54
خدا 54
خواب 54
پدر 54
زن 55
چ 58
چیز 59
خانه 61
بار 64
وقت 69
هر 72
پا 72
! 78
باز 81
برا 81
پ 81
ک 82
مثل 84
دا 86
صدا 89
کار 89
دو 90
ب 98
دس 100
مرد 104
می‌کرد 105
ما 106
ول 127
دیگر 139
: 140
« 142
سر 162
» 166
؟ 169
او 176
یک 225
، 723
. 1067

and for class 1 (old) :
قصر 18
غول 18
هیچ 19
رف 19
سه 19
ما 19
دا 19
سکه 20
فرزانه 20
زن 20
نه 21
دار 21
گاو 21
اینکه 21
گوساله 21
بازرگ 21
اگر 22
وقت 22
پا 22
تن 23
سو 23
دید 23
دیگر 24
بسیار 25
یا 25
خانه 26
بزرگ 26
دس 28
سفر 28
؟ 28
داد 28
چون 29
بعد 29
شاه 31
راه 31
مرا 31
ز 33
سال 33
هر 34
شب 34
عفر 34
دخ 35
پدر 37
پیر 37
پسر 38
کن 39
باز 40
کار 42
ا 42
مرد 43
یک 43
روز 44
سر 46
شهر 49
ب 51
برا 54
دو 64
او 68
برادر 72
: 85
. 235
، 613

