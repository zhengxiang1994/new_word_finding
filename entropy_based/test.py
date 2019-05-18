# -*- coding:utf-8 -*-

f = open('dict.txt', 'r')
dict = []

for word in f:
    dict.append(word.split(' ')[0])

print(dict)
