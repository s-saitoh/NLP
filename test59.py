# !/usr/bin/env python
# coding: utf-8
# python3系で動作
import os # ファイル操作のモジュール
import subprocess # コマンド実行のモジュール
import xml.etree.ElementTree as ET # XMLファイルの解析および作成のモジュール
import re # 正規表現

fname = 'nlp.txt'
fname_parsed = 'nlp.txt.xml'

# タグと内容を抽出するための正規表現
pattern = re.compile(r'''
    ^
    \(        # S式の開始カッコ
        (.*?) # ＝　タグ
        \s    # 空白
        (.*)  # ＝　内容
    \)        # s式の終わりのカッコ
    $
    ''', re.VERBOSE + re.DOTALL)

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
            ' -file ' + fname + ' 2>parse.out',
            shell=True,    # shellで実行
            check=True     # エラーチェックあり
        )
def ParseAndExtractNP(str, list_np):
    '''s式をタグと内容に分解し内容のみを返す
    またタグがNPの場合は、内容をlist_npにも追加する
    内容が入れ子になっている場合は、
    その中身も解析して、内容を空白区切りで返す。

    戻り値：
    タグを除いた内容
    '''

    # タグと内容を抽出
    match = pattern.match(str)
    tag = match.group(1)
    value = match.group(2)

    # 内容の解析
    # カッコで入れ子になっている場合は、一番外側を切り出して再帰
    depth = 0 # カッコの深さ
    chunk = '' # 切り出し中の文字列
    words = []
    for c in value:

        if c == '(':
            chunk += c
            depth += 1    # 深くなった

        elif c == ')':
            chunk += c
            depth -= 1    # 浅くなった
            if depth == 0: # 深さが0になった
                # 深さが戻ったので、カッコで区切られた部分の切り出し完了
                # 切り出した部分はParseAndExtractNP()に任せる(再帰呼び出し)
                words.append(ParseAndExtractNP(chunk, list_np))
                chunk = ''
        else:
            # カッコでくくられていない部分の空白は無視
            if not (depth == 0 and c == ' '):
                chunk += c

    # 最後の単語を追加
    if chunk != '':
        words.append(chunk)

    # 空白区切りに整形
    result = ' '.join(words)

    # NPならlist_npに追加
    if tag == 'NP':
        list_np.append(result)

    return result

# nlp.txtを解析
parse_nlp()

# 解析結果のxmlをパース
root = ET.parse(fname_parsed)

# sentence列挙、1文ずつ処理
for parse in root.iterfind('./document/sentences/sentence/parse'):
    result = []
    ParseAndExtractNP(parse.text.strip(), result)
    print(*result, sep='\n') # sepは区切り文字を指定するオプション

'''
*は可変長引数でどんな数の引数を渡しても対応できる
可変長で与えられた引数はタプル()として扱われる
今回は*resultとすることでresultすべてを引数として渡す
*がないとリストに入った状態で出力される
*があるとそれぞれ分割された文字列として出力される
'''
