#!/usr/bin/env python
#coding: utf-8
import sys

with open(sys.argv[1], encoding = "utf-8") as f:
    lines = f.readlines()

print(len(lines))
