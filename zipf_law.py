# -*- coding: utf-8 -*-
import sys
def modify_line(string):
    removing_character_string = "'‘’()<>[]{}&/?=-_:;,.!"
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



#--- main script ----
import math


fh = open(sys.argv[1], 'r')
word_list = []
line = fh.readline()
while line:
    wlist = modify_line(line).split()
    word_list.extend(wlist)
    line = fh.readline()
fh.close()

total_word_num = len(word_list)
print "Total Number of words =", total_word_num
word_frequency_dict = make_word_frequency_dictionary(word_list)

# 単語頻度で降順ソート、その単語出現確率 word_prob を求めて cvs 形式で出力
print "Sort by word probablility"
print "word, log(order), log(prob)"
order = 1
for word, freq in sorted(word_frequency_dict.items(), reverse=True, key = lambda x: x[1]):
    word_prob = float(freq) / total_word_num
    print "%s, %18.16f, %12.10f" % (word, math.log(order), math.log(word_prob) )
    order += 1
