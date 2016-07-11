# -*- coding: utf-8 -*-
import sys
def modify_line(string):
    removing_character_string = "‘’()<>[]{}&/?=-_:;,."
    modefied_str =string.lower()
    modefied_str = modefied_str.replace('"',' ')
    modefied_str = modefied_str.replace('\n','').replace('\t',' ')
    for s in removing_character_string:
        modefied_str = modefied_str.replace(s,' ')
    return(modefied_str)


# 単語リスト word_list から単語頻度辞書を作成
def make_word_frequency_dictionary(word_list):
    word_frequency_dict = {}
    for word in word_list:
        if word in word_frequency_dict:
            word_frequency_dict[word] += 1
    else:
        word_frequency_dict[word] = 1
    return(word_frequency_dict)


fh = open(sys.argv[1], 'r')
word_list = []
line = fh.readline()
while line:
    wlist = modify_line(line).split()
    word_list.extend(wlist)
    line = fh.readline()
fh.close()

word_frequency_dict = make_word_frequency_dictionary(word_list)
print word_frequency_dict
