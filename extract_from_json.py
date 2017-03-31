#!/usr/bin/env python
#coding: utf-8
import gzip
import json

def extract_from_json(title):
    with gzip.open("jawiki-country.json.gz") as f:
        json_data = f.readline()
        while article_json:
            article_dict = json.loads(json_data)
            if article_dict["title"] == title:
                return print(article_dict["text"])
            else:
                json_data = f.readline()
    return ""
