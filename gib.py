#!/usr/bin/python
"""
select random words from file and
print random length sentences.
"""

from random import randint
fo = open('words.txt', "rb")
lines = fo.readlines()
maxlines = len(lines)
paragraph_seed = randint(2, 9)
sentence_seed = randint(3, 15)

def gib(paragraphs, sentences):
    pghs = "" # paragraphs
    for z in range(0, paragraphs):
        pgh = "" # paragraph
        for y in range(0, sentences):
            words_seed = randint(3,18)
            words = ""
            for x in range(0, words_seed):
                random_line = randint(0, maxlines)
                words += lines[random_line].rstrip() + " "
            pgh +=  words.capitalize().rstrip() + ". "
        pghs += pgh + '\n' + '\n'
    return pghs

print(gib(paragraph_seed, sentence_seed))

fo.close()
