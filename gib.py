#!/usr/bin/python
"""
select random words from file and
print random length sentences.
"""

from random import randint
fo = open('words.txt', "rb")
lines = fo.readlines()
maxlines = len(lines)
sentence_seed = randint(3, 7)

def paragraph(num):
    paragph = ""
    for y in range(0, num):
        words_seed = randint(3,18)
        words = ""
        for x in range(0, words_seed):
            random_line = randint(0, maxlines)
            words += lines[random_line].rstrip() + " "
        paragph +=  words.capitalize().rstrip() + ". "
    return paragph

print(paragraph(sentence_seed))

fo.close()
