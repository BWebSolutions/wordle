"""
get_letter_values.py

Utility method to load the letter_values.txt 
and store in a dictionary
"""


def get_letter_values():
    # Load the file.
    with open('txt/wordle_letter_values.txt','r') as f:
        
        lines = f.read().splitlines()
        d = {}

        for line in lines:
            x = line.split(":")
            # print("{0}".format(line))
            d[x[0]] = int(x[1])

        return d


