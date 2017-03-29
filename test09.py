#!/usr/bin/env python
#coding: utf-8
import random

def word_typoglycemia(word):
    if len(word) <= 4:
        return word

    middle = list(word[1:-1])
    while middle == list(word[1:-1]):
        random.shuffle(middle)
    return word[0] + "".join(middle) + word[-1]

def str_typoglycemia(str):
    shuffled_list = []
    for word in str.split():
        shuffled_list.append(word_typoglycemia(word))
    return " ".join(shuffled_list)

str = "I couldn't believe that I could actually understand what I was reading :\
the phenomenal power of the human mind ."

print(str_typoglycemia(str))
