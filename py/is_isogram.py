"""
is_isogram.py

returns true if word contains all unique letters
"""


def is_isogram(string):
    for i in string:
        if string.count(i) > 1:
            return False
    return True