# !/usr/bin/env python
# coding: utf-8
# python3で実行
import re # 正規表現
import leveldb # 今回用いるKVS(Key Value Store)

fname_db = 'test_db'

# keyをnameとidに分解するための正規表現
pattern = re.compile(r'''
    ^       # 論理行頭
    (.*)    # name, 0文字以上の任意の文字列
    \t      # タブ区切り
    (\d+)   # id, 1文字以上の半角数字
    $       # 論理行末
    ''', re.VERBOSE + re.DOTALL)
    # re.VERBOSEは正規表現のパターンを読みやすくする
    # re.DOTALLはテキストが改行を含んでいるとき書く

# LevelDBオープン、なければ作成
db = leveldb.LevelDB(fname_db)

# 条件入力
clue = input('アーティスト名を入力してください　-->')
# Python2で動かす時はraw_inputに書き換えないとエラー
hit = False

# アーティスト名+'\t'で検索
for key, value in db.RangeIter(key_from=(clue + '\t').encode()):

    #keyをnameとidに戻す
    match = pattern.match(key.decode())
    name = match.group(1)
    id = match.group(2)

    # 異なるアーティストになったら終了
    if name != clue:
        break

    # 活動場所のチェック、表示
    area = value.decode()
    if area != '': # areaが空でないとき
        print('{}(id:{})の活動場所:{}'.format(name,id,area)) # formatで指定
    else:
        print('{}(id:{})の活動場所は登録されていません'.format(name,id))
    hit = True

if not hit:
    print('{}は登録されていません'.format(clue))
