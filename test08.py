#!/usr/bin/env python
#coding: utf-8
str = "Done is Better than Perfect."

def cipher(input):
    ret = ""
    for x in input:
        ret += chr(219-ord(x)) if x.islower() else x
    return ret

str = cipher(str)
print(str)
str = cipher(str)
print(str)
