"""
Counts the number of times each letter appears in a word
Adds the letter and count to letter_values.txt
"""


import os
from get_words import get_words
from string import ascii_lowercase

if __name__=="__main__":
	
	words = get_words()

	if os.path.exists("txt/wordle_letter_values.txt"):
		os.remove("txt/wordle_letter_values.txt")

	with open('txt/wordle_letter_values.txt', 'w') as f:
		for c in ascii_lowercase:
			cnt = 0
			for word in words:
				if word.find(c) >= 0:
					cnt += 1

			f.write("{0}:{1}\n".format(c, cnt))
			print("{0}:{1}".format(c, cnt))
