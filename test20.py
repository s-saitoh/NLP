#!/usr/bin/env python
#coding: utf-8
import gzip
import json

with gzip.open("jawiki-country.json.gz") as f:
    article_json = f.readline()
    while article_json:
        article_dict = json.loads(article_json)
        if article_dict["title"] == "イギリス":
            print(article_dict["text"])
        article_json = f.readline()
