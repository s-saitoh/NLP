# !/usr/bin/env python
# coding: utf-8
# python3で実行
import codecs # 文字コードの指定
import random

fname_pos = "rt-polaritydata/rt-polarity.pos"
fname_neg = "rt-polaritydata/rt-polarity.neg"
fname_smt = "sentiment.txt"
# rt-polarity.pos/rt-polarity.negのラテン文字に対応するためWINDOWS-1252を指定
fencoding = "cp1252"

result = []

# ポジティブデータの読み込み
with codecs.open(fname_pos, "r", fencoding) as file_pos:
    result.extend(['+1 {}'.format(line.strip()) for line in file_pos])
    # extendメソッドはリストの最後に別のリストの要素を追加

# ネガティブデータの読み込み
with codecs.open(fname_neg, "r", fencoding) as file_neg:
    result.extend(['-1 {}'.format(line.strip()) for line in file_neg])

# シャッフル
random.shuffle(result)

# 書き出し
with codecs.open(fname_smt, "w", fencoding) as file_out:
    print(*result, sep='\n', file=file_out) # sepは区切りの指定
    # 引数の展開に*や**が使えるのは3系、2系ではapply()を使う

# 数の確認
cnt_pos = 0
cnt_neg = 0
with codecs.open(fname_smt, "r", fencoding) as file_out:
    for line in file_out:
        if line.startswith('+1'):
            cnt_pos += 1
        elif line.startswith('-1'):
            cnt_neg += 1

print('pos:{}, neg:{}'.format(cnt_pos, cnt_neg))
