# !/usr/bin/env python
# coding: utf-8

# stopwordのリスト　http://xpo6.com/list-of-english-stop-words/ のCSV Formatより

stop_words = (
    'a,able,about,across,after,all,almost,also,am,among,an,and,any,are,'
    'as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,'
    'either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,'
    'him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,'
    'likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,'
    'on,only,or,other,our,own,rather,said,say,says,she,should,since,so,'
    'some,than,that,the,their,them,then,there,these,they,this,tis,to,too,'
    'twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,'
    'will,with,would,yet,you,your').lower().split(',')
    # lower()は文字列を小文字に変換

def is_stopword(str):
    '''文字がストップワードかどうかを返す
    大小文字は同一視する

    戻り値：
    ストップワードならTrue, 違う場合はFalse
    '''

    return str.lower() in stop_words

# 正しく検出されることのテスト
# assert文は開発中のチェックにしか使えない
assert is_stopword('a')
assert is_stopword('your')
assert is_stopword('often')
assert is_stopword('Neither')
assert is_stopword('wherE')
assert is_stopword('AMONG')

# 誤検出されないことのテスト, AssertionErrorに引っかかる
assert is_stopword('0')
assert is_stopword('fte')
assert is_stopword(' ')
assert is_stopword('\n')
assert is_stopword('')
