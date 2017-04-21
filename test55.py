# !/usr/bin/env python
# coding: utf-8
import os # ファイル操作のモジュール
import subprocess # コマンド実行のモジュール
import xml.etree.ElementTree as ET # XMLファイルの解析および作成のモジュール

fname = 'nlp.txt'
fname_parsed = 'nlp.txt.xml'

def parse_nlp():
    '''
    nlp.txtをStanford Core NLPで解析しxmlファイルに出力
    すでに結果ファイルが存在する場合は実行しない
    '''

    if not os.path.exists(fname_parsed): # 「結果ファイルがある」の否定

        # StanfordCoreNLP実行、標準エラーはparse.outに出力
        subprocess.check_output( # 3.5以上だとrun関数を使う
            ' java -cp "/usr/local/lib/stanford-corenlp-full-2016-10-31/*"'
            ' -Xmx2g'
            ' edu.stanford.nlp.pipeline.StanfordCoreNLP'
            ' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
            ' -file ' + fname,
            shell=True,    # shellで実行
            check=True     # エラーチェックあり
        )

# nlp.txtを解析
parse_nlp()

# 解析結果のxmlをパース
root = ET.parse(fname_parsed)

# tokenの抽出
for token in root.iterfind(
    './document/sentences/sentence/tokens/token[NER="PERSON"]'
): # xmlでのイテレート処理（繰り返し）
    print(token.findtext('word'))
