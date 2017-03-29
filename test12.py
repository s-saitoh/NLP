#!/usr/bin/env python
#coding: utf-8
import sys

def write_column(txt_lines, column_num, filename):
    col = []
    for line in txt_lines:
        col.append(line.split()[column_num] + "\n")
    with open(filename, "w") as writer:
        writer.writelines(col)

with open(sys.argv[1], encoding = "utf-8") as f:
    lines = f.readlines()

write_column(lines, 0, "col1.txt")
write_column(lines, 1, "col2.txt")
