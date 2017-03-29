#!/usr/bin/env python
#coding: utf-8

import sys

filename = sys.argv[1]
prefs = set()

with open(filename, encoding = "utf-8") as f:
    line = f.readline()
    while line:
        prefs.add(line.split()[0])
        line = f.readline()

for pref in prefs:
    print(pref)
