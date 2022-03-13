"""
create_word_values.py

Utility to get the best wordle words based on the most common letters
"""

import os
import operator
from get_letter_values import get_letter_values
from get_words import get_words
from is_isogram import is_isogram

dict_lv = get_letter_values()
words = get_words()
isogram_words = []
d = {}

for word in words:
    score = 0
    for c in word:
        score += dict_lv[c] 

    d[word] = score

sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))

if os.path.exists("txt/wordle_rank.txt"):
	os.remove("txt/wordle_rank.txt")

"""
with open('txt/word_values.txt', 'w') as f:
    for key, val in sorted_d.items():
        f.write("{0}:{1}\n".format(key, val))

if os.path.exists("txt/isogram_values.txt"):
	os.remove("txt/isogram_values.txt")
"""
with open('txt/wordle_values.txt', 'w') as f:
    for key, val in sorted_d.items():
        if is_isogram(key):
            f.write("\"{0}\",".format(key, val))

    for key, val in sorted_d.items():
        if not is_isogram(key):
            f.write("\"{0}\",".format(key, val))
        
  