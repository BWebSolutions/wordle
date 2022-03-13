"""
is_in_string.py

recursive function to check if all of search characters are in given string
"""


def is_in_string(s, string):

    if len(s) == 0:
        return True
    
    if s[0] not in string:
        return False
    else:
        return is_in_string(s[1:], string)


def is_not_in_string(s, string):

    if len(s) == 0:
        return True
    
    if s[0] in string:
        return False
    else:
        return is_not_in_string(s[1:], string)
    
    