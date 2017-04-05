#!/usr/bin/env python
#coding: utf-8
import random


def word_typoglycemia(word):
    if len(word) <= 4:
        return word

    mid_list = list(word[1:-1])
    while mid_list == list(word[1:-1]):
        random.shuffle(mid_list)
    return word[0] + "".join(mid_list) + word[-1]


def str_typoglycemia(str):
    shuffled_list = []
    for word in str.split():
        shuffled_list.append(word_typoglycemia(word))
    return " ".join(shuffled_list)


str = "I couldn't believe that I could actually understand \
 what I was reading : the phenomenal power of the human mind ."

print(str_typoglycemia(str))
