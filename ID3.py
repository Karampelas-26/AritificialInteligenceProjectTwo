import os
from numpy import log1p as log
import numpy as np
import pandas as pd
import sklearn

my_path = "C:\\Users\\User\\Desktop\\project2\\aclImdb"

class Node:
    def __init__(self, pos_sum, neg_sum):
        self.value = None
        self.pos_sum = pos_sum
        self.neg_sum = neg_sum
        self.total_percentage = None
        self.right = None
        self.left = None
        self.result = None



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

    # fileCount = len(os.listdir(path))

    for word in dictionary.keys():
        dictionary[word]=0

    # dictionary["fileCount"] = fileCount

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



def entropy(word, pos_dict, neg_dict):
        propability_pos = propability_neg = propability_log_pos = propability_log_neg = 0.0

        if word in pos_dict:
            if word in neg_dict:
                propability_pos = pos_dict[word] / neg_dict[word] + pos_dict[word]
            else:
                propability_pos = 1
        else:
            propability_pos = 1 / pow(25000, 2)

        if word in neg_dictionary:
            if word in pos_dict:
                propability_neg = neg_dict[word] / neg_dict[word] + pos_dict[word]
            else:
                propability_neg = 1
        else:
            propability_neg = 1 / pow(25000, 2)

        propability_log_pos = log(propability_pos)
        propability_log_neg = log(propability_neg)



        return -propability_pos*propability_log_pos - propability_neg*propability_log_neg

def informationGain(word, pos_dict, neg_dict): # legit douleuei

    infoGain = 0.0

    entropia = entropy(word, pos_dict, neg_dict)

    if word in pos_dict.keys() & neg_dict.keys():
        infoGain += 1 -( (neg_dict[word]+pos_dict[word])/25000  * entropia +((12500 -pos_dict[word]) + (12500 -neg_dict[word])/25000) *(1-entropia) )

    return infoGain



# class ID3Tree: #/// thelei doyleia edw...///#
#     def create_tree(self, pos_dict, neg_dict, all_dict, d):
#         root = Node(None, 0, 0)
#         node = Node(word, neg, pos)
#         if len(all_dict) == 0:
#             node.result = 1 if len(pos) < len(neg) else -1
#             return node
#         elif len(pos) == 0 and len(neg) == 0:
#             node.result = d
#             return node
#         elif len(pos) == 0:
#             node.result = 1
#             return node
#         elif len(neg) == 0:
#        yy6666666     node.result = -1
#             return node
#
#         node.word = word
#         if (word exists):
#             node.right = ID3Tree()
#         else:
#             node.left = ID3Tree()
#
#
#         return node
#

# Second failed try
# class ID3:
#     def create(self, pos_dict, neg_dict, all_dict, d):
#         node = Node(pos_dict, neg_dict)
#
#
#
#         if len(all_dict) == 0:
#             return
#
#         #find max gain
#         max = 0
#         maxWord = None
#         for word in all_dict.keys():
#             info = informationGain(word, pos_dict, neg_dict)
#             if info > max:
#                 max = info
#                 maxWord = word
#
#         temp_dict = all_dict
#         del temp_dict[maxWord]
#
#         node.value = maxWord
#
#
#     def addNode(self, node, value):
#         if (node.left == None):
#             node.left = value
#             return node
#         else:
#             node.right = value
#             return node


def ID3(pos_dict, neg_dict, all_dict, parent = None):
    if len(all_dict) == 0:
        return parent
    elif len(pos_dict)/len_pos <= 0.3: #katw apo 30% toy len toy leksikou me tis 8etikes lekseis return
        return 1
    elif len(neg_dict)/len_neg <= 0.3: #katw apo 30% toy len toy leksikou me tis arntikes lekseis return
        return -1
    else:


        # item_values = [informationGain(word, pos_dict, neg_dict) for word in all_dict.keys()] #ypologise gia all_dict infogain
        # maxInfo = np.argmax(item_values) #bres to index gia to megalytero IG

        if len(all_dict) > 0:
            maxValue = 0
            maxInfo = "tipota"
            for key in all_dict:
                # print(key)
                temp = informationGain(key, pos_dict, neg_dict)
                # print(temp)
                if abs(temp) > maxValue:
                    maxValue = temp
                    maxInfo = key

            # print(maxValue)
            # print(maxInfo)
            # print(all_dict)
            # print(all_dict[maxInfo])
            best_word = maxInfo #i leksi me to megalutero IG
            if best_word in pos_dict.keys() & neg_dict.keys():
                parent_node = 1 if pos_dict[best_word] > neg_dict[best_word] else -1
            elif best_word not in pos_dict:
                parent_node = -1
            else:
                parent_node = 1
            new_pos_dict = pos_dict
            new_neg_dict = neg_dict
            new_all_dict = all_dict
            # print(all_dict[best_word])
            new_all_dict.pop(maxInfo)
            if best_word in pos_dict:
                new_pos_dict.pop(maxInfo)
            if best_word in neg_dict:
                new_neg_dict.pop(maxInfo)

            tree = {best_word: {}}

            subtree = ID3(new_pos_dict, new_neg_dict, new_all_dict, parent_node)

            tree[best_word] = subtree
            return tree

def prediction(text, tree, default = 1):
    result = default
    subtree = None
    for key in text:
        for key in tree.keys():
            #print(key)
            subtree = tree[key]
           # print(pos_dictionary)
            if key in pos_dictionary.keys() & neg_dictionary:
                if pos_dictionary[key] > neg_dictionary[key]:
                    result = 1
                elif neg_dictionary[key] > pos_dictionary[key]:
                    result = -1
                else:
                    result = default
            elif key not in pos_dictionary.keys():
                result = -1
            else:
                result = 1
       # except:
           # return default
        if isinstance(subtree, dict):
            return prediction(text, subtree)
        else:
            return result

def test(myfile):
    path = my_path + '\\test\\' + str(myfile)
    neg_result = pos_result  = 0
    for filename in os.listdir(path):
        with open(os.path.sep.join([path, filename]), encoding="utf8") as f:
            text = f.read()
            text = clean(text)
            temp = prediction(text, tree, 1)
            if temp == 1:
                pos_result += 1
            else:
                neg_result += 1

    return pos_result , neg_result


# def Classify(text):
#     currentNode = root
#     result = None
#     while currentNode.word is not None:
#         result = currentNode.result
#         if currentNode.word in text:
#             currentNode = currentNode.right
#         else:
#             currentNode = currentNode.left
#     return result


if __name__ == '__main__':
    pos_dictionary = train("pos")
    neg_dictionary = train("neg")
    len_pos = len(pos_dictionary)
    len_neg = len(neg_dictionary)
    # all_dict = set()
    # all_dict = pos_dictionary.union(neg_dictionary)
    # for key in pos_dictionary.keys():
    #     all_dic.add(key)
    # for kei in neg_dictionary.keys():
    #     all_dic.add(key)
    all_dict = pos_dictionary
    for key, value in neg_dictionary.items():
        if key in all_dict:
            all_dict[key] += value
        else:
            all_dict[key] = value

    # del all_dict['']
    all_dict.pop('')


    print('tree')

    tree = ID3(pos_dictionary, neg_dictionary, all_dict)
    print(tree)
    pos1 , pos2 = test("pos")
    neg1 , neg2 = test("neg")
    print ("positive => "+str(pos1)+ " " +str(pos2))
    print ("negative => "+str(neg1)+ " " + str(neg2))






