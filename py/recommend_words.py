"""
recommend_words.py

recommends isograms and other 5 letter words based on input string
"""

from is_in_string import is_in_string, is_not_in_string


words = []
showwords = []

with open('txt/isogram_values.txt','r') as f:
    lines = f.read().splitlines()

    for line in lines:
        x = line.split(":")
        words.append(x[0])

with open('txt/non_isogram_values.txt','r') as f:
    lines = f.read().splitlines()

    for line in lines:
        x = line.split(":")
        words.append(x[0])



def search_words(search, search_incorrect, words):
    if search[-4:] == 'quit':
        quit()
    
    showwords.clear()

    for word in words:
        if is_in_string(search, word) and is_not_in_string(search_incorrect, word):
            showwords.append(word)

    """
    for i in range(len(words)):
        if i <= 50:
            showwords.append(words[i])
    """

    print("-"*100)
    print(showwords[:50])
    print("-"*100)
    print()

    inp = input("Enter correct letters: {0}".format(search))
    search += inp

    inp = input("Enter incorrect letters: {0}".format(search_incorrect))
    search_incorrect += inp
    
    search_words(search, search_incorrect, words)

    

search_words('', '', words)