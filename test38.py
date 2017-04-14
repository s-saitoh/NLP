#!/usr/bin/env python
#coding: utf-8
import MeCab
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fname = 'neko.txt'
fname_parsed = 'neko.txt.mecab'

def parse_neko():
    "「吾輩は猫である」を形態素解析してneko.txt.mecabに保存"

    with open(fname) as data_file, \
        open(fname_parsed, mode="w") as out_file:
        mecab = MeCab.Tagger()
        out_file.write(mecab.parse(data_file.read()))

def neko_lines():
    """「吾輩は猫である」の形態素解析結果のジェネレータ
    解析結果を読み込んで各形態素を
    表層形(surface)
    基本形(base)
    品詞(pos)
    品詞細分類1(pos1)
    をキーとするマッピング型に格納し、1文を形態素のリストとして表現

    戻り値：
    1文の各形態素を辞書化したリスト
    """
    with open(fname_parsed) as file_parsed:

        morphemes = []# 格納するリスト
        for line in file_parsed:

            #表層形はtab区切り、それ以外は","区切りでばらす
            cols = line.split("\t") #tab区切り
            if(len(cols) < 2):
                raise StopIteration #区切りがなければ終了
            res_cols = cols[1].split(",")#それ以外は”,”で区切る

            #辞書作成、リストに追加
            morpheme = {
                "surface" : cols[0],
                "base" : res_cols[6],
                "pos" : res_cols[0],
                "pos1" : res_cols[1]
            }
            morphemes.append(morpheme)

            #品詞細分類1が句点なら文の終わりと判定
            if res_cols[1] == '句点':
                yield morphemes
                morphemes = []

#形態素解析
parse_neko()

# Counterオブジェクトに単語をセット
word_counter = Counter()
# collections.Counter オブジェクトはイテレータを渡すと{要素, カウント}の辞書を作成
for line in neko_lines():
    word_counter.update([morpheme['surface'] for morpheme in line]) # updateで1行ずつ追加

# 全件取得
list_word = word_counter.most_common()

# 出現数のリスト取得
counts = list(zip(*list_word))[1]

# グラフで使うフォント情報（デフォルトのままでは日本語が表示できない）
"""
fp = FontProperties(
    fname='/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf'
)
"""

# ヒストグラムのデータ指定
plt.hist(
    counts,        # データのリスト
    bins=20,        # ピンの数
    range=(1, 20))

# X軸の値の範囲の調整
plt.xlim(xmin=1, xmax=20)

#グラフのタイトル、ラベル指定
"""
plt.title("38. ヒストグラム", fontproperties=fp)
plt.xlabel('出現頻度', fontproperties=fp)
plt.ylabel('単語の種類数', fontproperties=fp)
"""

# グリッドを表示
plt.grid(axis='y')

# 表示
plt.show()

# 日本語フォントを表示しようとするとエラーが出る問題は未解決
# ref. http://symfoware.blog68.fc2.com/blog-entry-1417.html
