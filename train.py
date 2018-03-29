import re
import json
import argparse

d = {}

def push(word1, word2):
    if word1 in d:
        if word2 in d[word1]:
            d[word1][word2] += 1
        else:
            d[word1][word2] = 1
    else:
        d[word1] = {}
        d[word1][word2] = 1

def StrBreak(s, LastWord):   # разбивка строки, кидаю посл слово с перд строки
    s = s.lower()
    s = re.sub('ё', 'е', s)
    s = re.sub('[^а-яА-Я ]', '', s)

    words = s.split(' ')
    if LastWord != '':    # связываю первое слово с последним в пред. строке
        push(LastWord, words[0])

    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        if word1 != '' and word2 != '':  # сплит пробелы превращаяет в ''
            push(word1, word2) # добавляю word2 в d[word1]

    LastWord = words[len(words)-1]  #сохраняю последнее слово и возвращаю
    return LastWord


def MakeDict():
    f = open('text', 'r')
    LastWord = ''
    for line in f:
        LastWord = StrBreak(line, LastWord)
    f.close()


MakeDict()
json.dump(d, open('dictionary', 'w'))
