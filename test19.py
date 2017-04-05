#!/usr/bin/env python
#coding: utf-8
import sys
from collections import defaultdict

filename = sys.argv[1]
prefs = defaultdict(int)
with open(filename, encoding = "utf-8") as f:
    line = f.readline()
    while line:
        prefs[line.split()[0]] += 1
        line = f.readline()

for k , v in sorted(prefs.items(), key = lambda x: x[1], reverse = True):
    print(k)
