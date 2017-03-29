#coding: utf-8
str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. \
New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str1 = str1.split()
dict1 = {}

for i,x in enumerate(str1, start=1):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        dict1[x[:1]] = i
    else:
        dict1[x[:2]] = i

print(sorted(dict1.items(), key=lambda x:x[1]))
