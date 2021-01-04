import os
from os import listdir
from os.path import isfile, join
import string


my_path = 'C:\\Users\\georg\\OneDrive - aueb.gr\\artificial_intelligence\\assignment_2\\aclImdb\\train\\pos'


def read(my_file):
    reader = open(my_file, 'r')
    word = str(reader.readlines())
    word = word.replace('\n', '')
    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.replace(':', '')
    word = word.replace('?', '')
    word = word.replace('*', '')
    word = word.replace('!', '')
    word = word.replace('/', '')
    arr  = word.split()
    print(arr)
    reader.close()




def read_all_files():
    onlyfiles = [f for f in listdir(my_path) if isfile(join(my_path, f))]

    for file in onlyfiles:
        read(file)

# def read():
#     new_list = []
#     for root, dirs, files in os.walk(my_path):
#         for file in files:
#             if file.endswith('.txt')
#                 with open(os.path.join(root, file), 'r') as f:
#                     text = f.read()
#                     new_list.append(text)
#


if __name__ == '__main__':
     read_all_files()