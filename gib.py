#!/usr/bin/python
"""
select random words from file and
print random length sentences.
"""

from random import randint
fo = open('words.txt', "rb")
lines = fo.readlines()
maxlines = len(lines)

 # seed words per sentence
sentence_seed = randint(3, 6)
def sentence():
    words_seed = randint(3,18)
    str = ""
    for x in range(0, words_seed):
        random_line = randint(0, maxlines)
        str += lines[random_line].rstrip() + " "

    return str.capitalize().rstrip() + "."

# print str.capitalize().rstrip() + "."
print(sentence())

fo.close()
