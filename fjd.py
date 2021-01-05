import os
import os
from os import listdir
from os.path import isfile, join
import string

wf = open('stop_words.txt', mode='r',encoding='utf8')
file = wf.readlines()
print(file)
lst = list()
for f in file:
    f = f.replace('\n', ' ')
    lst.append(f)
wf = open('stop_words.txt', mode='w',encoding='utf8')
for i in lst:
    wf.write(i)
print(lst)


