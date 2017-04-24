# !/usr/bin/env python
# coding: utf-8
#python2,python3どちらも実行可能

import leveldb # 今回用いるKVS(Key Value Store)

fname_db = 'test_db'

# LevelDBオープン
db = leveldb.LevelDB(fname_db)

# Valueが'Japan'のものを列挙
clue = 'Japan'.encode('utf-8')
result = [value[0].decode('utf-8') for value in db.RangeIter() if value[1] == clue]

# 件数表示
print('{}件見つかりました'.format(len(result)))
