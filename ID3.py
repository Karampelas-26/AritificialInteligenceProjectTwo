import os
from numpy import log1p as log

my_path = 'C:\\Users\\georg\OneDrive - aueb.gr\\artificial_intelligence\\assignment_2\\aclImdb'

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

    for word in dictionary.keys():
        dictionary[word]=0

    dictionary["fileCount"] = fileCount

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

    for word in list(dictionary.keys()):
        if (dictionary[word] < 1000): #100ari camel 8ew mouni
            dictionary.pop(word)

    # for k, v in dictionary.items():
    #     print(k+ " "+str(v))
    # print(len(dictionary))
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
        propability_pos = propability_neg = propability_log_pos = propability_log_neg = 0.0

        if node.value in pos_dictionary:
            propability_pos = pos_dictionary[node.value] / node.neg_sum+node.pos_sum
        else:
            propability_pos = 1 / 25000^2

        if node.value in neg_dictionary:
            propability_neg = neg_dictionary[node.value] / node.neg_sum+node.pos_sum
        else:
            propability_neg = 1 / 25000^2

        propability_log_pos = log(propability_pos)
        propability_log_neg = log(propability_neg)

        return -propability_pos*propability_log_pos - propability_neg*propability_log_neg

def informationGain():




    return


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
    neg_dictionary = train("neg")


