import os
import csv
from os import listdir
from os.path import isfile, join
import string
from collections import Counter

my_path = 'C:\\Users\\georg\\OneDrive - aueb.gr\\artificial_intelligence\\assignment_2\\aclImdb\\train'

def stop_words_to_list():
    lst = []
    with open('stop_words.txt', "r") as file:
        lst = file.read().split()
    return lst

def save(file, dictionary):
    with open(file, 'w', newline='', encoding='utf8') as csvFile:
        spam_writer = csv.writer(csvFile, delimiter = ' ')
        for keys, value in dictionary.items():
            spam_writer.writerow([keys] + [value])
#it is working
def clean(word):
    stopWords = stop_words_to_list()
    word = word.lower()
    word = word.replace('\n', '')
    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.replace(':', '')
    word = word.replace('?', '')
    word = word.replace('*', '')
    word = word.replace('!', '')
    word = word.replace('"', '')
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
    text = word.split(' ')
    text = [t for t in text if t not in stopWords]
    return text

def train(myfile):

    path = my_path + '\\' + str(myfile)
    dictionary = {}
    for filename in os.listdir(path):
        with open(os.path.sep.join([path, filename]), encoding="utf8") as f:
            text = f.read()
            text = clean(text)
            for word in text:
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1

    fileCount = len(os.listdir(path))
    for word in dictionary.keys():
        dictionary[word] = float(dictionary[word]) / fileCount
    dictionary["fileCount"] = fileCount
    return dictionary


if __name__ == '__main__':
    save('pos.csv', train('pos'))
    save('neg.csv', train('neg'))
