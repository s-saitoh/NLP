#!/usr/bin/env python
#coding: utf-8
from mymodule import ex_from_json

lines = ex_from_json.extract_from_json(u"イギリス").split("\n")

for line in lines:
    if "Category" in line:
        print(line)

#print([line for line in lines if "Category" in line])
