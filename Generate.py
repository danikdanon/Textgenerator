import json
import random

d = json.load(open('dictionary',  'r'))  # загрузил созданнный словарик


def NextWord(curr):
    if curr not in d:
        return random.choice(list(d))

    l = []   # я создаю список с дубликатами из всех слов
    for word in d[curr]:
        cnt = d[curr][word]
        l.extend([word]*cnt)

    if (len(l) == 0):
        return random.choice(list(d))
    else:
        return random.choice(l)


textlen = 2000
curr = random.choice(list(d))
ans = ''
str_cnt = 0
str_len = 75
while (len(ans) < textlen):
    ans += curr + ' '
    curr = NextWord(curr)
    if (len(ans) - str_cnt*str_len > str_len):  # если строка слишком длинная
        ans += '\n'
        str_cnt += 1

file = open('result', 'w')
file.write(ans)
