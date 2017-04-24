# !/usr/bin/env python
# coding: utf-8
import gzip # gzファイル解凍モジュール
import json
import leveldb # 今回用いるKVS(Key Value Store)

fname = 'artist.json.gz'
fname_db = 'test_db'

# LevelDBオープン、なければ作成
db = leveldb.LevelDB(fname_db)

# gzファイル読み込み、パース
with gzip.open(fname, 'rt') as data_file:
    for line in data_file:
        data_json = json.loads(line, encoding = 'utf-8')

        # key=name+id, value=areaとしてDBに追加
        key = data_json['name'] + '\t' + str(data_json['id'])
        value = data_json.get('area')
        if value is None:
            value = '' # value（area、活動場所）が空のときは空にしておく
        db.Put(key.encode('utf-8'), value.encode('utf-8')) # 文字列からバイト列に変換

# 確認のため登録件数を表示
print('{}件登録しました。'.format(len(list(db.RangeIter(include_value=False)))))
