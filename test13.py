#!/usr/bin/env python
#coding: utf-8
import sys

with open("col1.txt") as f1, open ("col2.txt") as f2:
    line1, line2 = f1.readlines(), f2.readlines()

with open("merge.txt", "w") as writer:
    for col1, col2 in zip(line1, line2):
        writer.write("\t".join([col1.rstrip(), col2]))
