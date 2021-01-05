import os
from os import listdir
from os.path import isfile, join
import string
from collections import Counter

pos_file = open('stop_words_pos.txt', encoding='utf8')
neg_file = open('stop_words_neg.txt', encoding='utf8')
pos_set = set()
neg_set = set()
for f in pos_file:
    f = f.replace('(')
    f = f.replace(')')
    arr = f.split(',')
    f = f.replace('a', 'dkdkkdkdkdkdkdkdk')
    print(arr[0])
    pos_set.add(f)

# print(pos_set)


