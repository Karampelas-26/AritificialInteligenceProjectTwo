import os

my_path = 'C:\\Users\\georg\\OneDrive - aueb.gr\\artificial_intelligence\\assignment_2\\aclImdb'

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
    return dictionary

class ID3Tree:
    def create_tree(self, pos_dict, neg_dict):
        root = Node(None, 0, 0)

    def addNode(self, node, value):
        if (node.left == None):
            node.left = value
        else:
                node.right = value


if __name__ == '__main__':
    train("pos")
    train("neg")