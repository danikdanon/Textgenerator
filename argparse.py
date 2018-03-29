Артур Мутолапов, [28 марта 2018 г., 18:49:47]:
...# using argparse library to parse commands in command line
parser = argparse.ArgumentParser(description='generate')
parser.add_argument(
    '--model',
    default='/home/artur/PycharmProjects/TextGenerator/model',
    help='file from which model downloads'
)
parser.add_argument(
    '--seed',
    default='#',
    help='first word of the text'
)
parser.add_argument(
    '--length',
    default=1000,
    help='length of the text'
)
parser.add_argument(
    '--output',
    default='/home/artur/PycharmProjects/TextGenerator/RandomText',
    help='output file'
)

# getting data from command line
namespace = parser.parse_args(sys.argv[1:])

# importing histogramm from model
hist = {}
hist = json.load(open(namespace.model, 'r'))

# getting next word using histogramm
def get_next_word(word):
    sum = 0
    if word not in hist:
        word = random.choice(list(hist.keys()))
    tmpList = []
    for nextWord in hist[word]:
        tmpList.append(nextWord)
    return random.choice(tmpList)


# first word, length, number of strings, random text
currentWord = namespace.seed
if currentWord == '#':
    currentWord = random.choice(list(hist))
textLength = int(namespace.length)
s = currentWord + ' '
numberOfStrings = 1

# building random text 's' with 'textLength' length
while len(s) < textLength:
    tmpWord = get_next_word(currentWord)
    currentWord = tmpWord
    s += tmpWord + ' '
    if len(s) > 50 * numberOfStrings:
        s += '\n'
        numberOfStrings += 1

# writing random text to the file
file = open(namespace.output, 'w')
file.write(s)
file.close()

# -*- coding: utf-8 -*-
import re
import json
import argparse
import sys
import os

# using argparse library to parse commands in command line
parser = argparse.ArgumentParser(description='train')
parser.add_argument(
    '--input-dir',
    default='#',
    help='directory from which texts download'
)
parser.add_argument(
    '--model',
    default='/home/artur/PycharmProjects/TextGenerator/model',
    help='file in which histogramm downloads'
)

# getting data from command line
namespace = parser.parse_args(sys.argv[1:])

# histogramm which downloads into model
hist = {}
...