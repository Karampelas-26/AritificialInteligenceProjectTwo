import os
from numpy import log2 as log

my_path = 'C:\\Users\plaisio\\downloads\\aclImdb'

class Node:
    def __init__(self, value, pos_sum, neg_sum):
        self.value = value
        self.pos_sum = pos_sum
        self.neg_sum = neg_sum
        self.total_percentage = None
        self.right = None
        self.left = None


def stop_words_to_list():
    lst = []
    with open('stop_words.txt', "r") as file:
        lst = file.read().split()
    return lst

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
    path = my_path + '\\train\\' + str(myfile)
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
    for word in list(dictionary.keys()):
        if (dictionary[word] < 50):
            dictionary.pop(word)
    dictionary["fileCount"] = fileCount
    
    for word in dictionary.keys():
        dictionary[word]=0

    for filename in os.listdir(path): #for gia na exei mesa to dictionary
                                        # poses fores emfanizetai sta arxeia
                                        #i kathe leksi
        with open(os.path.sep.join([path, filename]), encoding="utf8") as f:
            text = f.read()
            text = clean(text)
            counted_words = set() #gia kathe arxeio blepoume poies lekseis exoume idi dei
            for word in text:
                if word in dictionary:
                    if word not in counted_words:
                        dictionary[word] += 1
                    else:
                        counted_words.add(word)

    return dictionary

# def test(myfile):
#     path = my_path + '\\train\\' + str(myfile)
#     review_words = set()
#
#
#     for filename in os.listdir(path):
#         with open(os.path.sep.join([path, filename]), encoding="utf8") as f:
#             text = f.read()
#             text = clean(text)
#



def entropy(node):
    ent =
class ID3Tree:
    def create_tree(self, pos_dict, neg_dict):
        root = Node(None, 0, 0)

    def addNode(self, node, value):
        if (node.left == None):
            node.left = value
        else:
            node.right = value


if __name__ == '__main__':
    pos_dictionary = train("pos")
    #neg_dictionary = train("neg")