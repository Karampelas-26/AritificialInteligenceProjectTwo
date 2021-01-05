def func():
    pos_file = open('stop_words_pos.txt', encoding='utf8')
    neg_file = open('stop_words_neg.txt', encoding='utf8')

    pos_set = set(pos_file.readlines())
    neg_set = set(neg_file.readlines())

    both_set = pos_set | neg_set

    wfile = open('stop_words.txt', mode='w', encoding='utf8')

    for w in both_set:
        wfile.write(w)

if __name__ == '__main__':
     # read_all_files()
    func()