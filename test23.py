#!/usr/bin/env python
#coding: utf-8
import gzip
import json
import re # 正規表現
filename = "jawiki-country.json.gz"

def extract_UK():
    # イギリスの本文を戻り値として取得

    # rtは読み込み専用＆テキストモード（いずれもデフォルト）
    with gzip.open(filename, "rt", encoding = "utf-8") as data_file:
        for line in data_file:
            data_json = json.loads(line)# jsonのデータをロードしてpythonのデータ型に変換
            if data_json["title"] == "イギリス":# タイトルが「イギリス」の時
                return data_json["text"]# 本文を戻り値として返す

    raise ValueError("Not Found Article About UK")
    # タイトルがイギリスでないとき例外処理としてValueErrorを出す


# 正規表現のコンパイル、あらかじめ使う正規表現を書き込んでおく
pattern = re.compile(r'''
    ^       # 行頭
    (={2,}) # キャプチャ対象、2個以上の'='
    \s*     # 余計な0個以上の空白（”哲学”や”婚姻”の前後に余分な空白があるため除去）
    (.+?)   # 余分な0個以上の空白
    \1      # 後方参照、1番目のキャプチャ対象と同じ内容
    .*      # 任意の文字が0文字以上
    $       # 行末
    ''', re.MULTILINE + re.VERBOSE)
    # MULTILINEは読み込みが複数行あるため、VERBOSEは正規表現中にコメントするため

# 抽出
result = pattern.findall(extract_UK())#findallはマッチした部分だけを持ってくる

# 結果表示
for line in result:
    level = len(line[0]) - 1 #"="の数 - 1
    print("{indent}{sect}({level})".format( #format関数を使用
    indent = "\t" * (level -1), sect = line[1], level = level))
