import os
from os import listdir
from os.path import isfile, join
import string
from collections import Counter

my_path = 'C:\\Users\\georg\\OneDrive - aueb.gr\\artificial_intelligence\\assignment_2\\aclImdb\\train'

stopWordsFile = open('stop_words.txt')
stopWords = set(stopWordsFile.readlines())

def clean(word):
    word = word.lower()
    word = word.replace('\n', '')
    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.replace(':', '')
    word = word.replace('?', '')
    word = word.replace('*', '')
    word = word.replace('!', '')
    word = word.replace('/', '')
    word = word.replace('(', '')
    word = word.replace(')', '')
    word = word.replace('-', '')
    word = word.replace('&', '')
    word = word.replace('<br />','')
    word = word.replace('//>','')
    word = word.replace('/>','')
    word = word.replace('<br','')
    word = word.replace('/><br','')
    word = word.replace('<','')
    word = word.replace('>','')
    word = word.replace('<br>','')
    word = word.replace('<br >','')
    word = word.replace('\\', '')
    word = [w for w in word if w not in stopWords]
    return word

def read_common(choice):
    count = Counter()
    arr = []
    path = my_path + '\\' + choice
    for filename in os.listdir(path):
        with open(os.path.sep.join([path, filename]), encoding="utf8") as f:
            for line in f.readlines():
                line = clean(line)
                line = line.strip()
                # count all words in line
                count.update(line.split())
    arr = count.most_common(500)





if __name__ == '__main__':
    read_common()