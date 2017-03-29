#coding: utf-8
def n_gram(text, n, mode = "word"):
    """
    Args:
    text: 対象の文字列
    n: Nの値
    mode: 単語で区切るなら「word」,　文字で区切るなら「char」.デフォルトはword
    Return:
    n_gram: N-gramで分解した結果
    """

    n_gram = []
    if (mode == "word"):
        chars = text.split()
    elif(mode == "char"):
        chars = text.replace(" ", "")

    first_n = n
    while n - 1 < len(chars):
        n_gram.append(chars[n - first_n: n])
        n += 1

    return n_gram

str1 = "paraparaparadise"
str2 = "paragraph"

x = n_gram(str1, 2, "char")
y = n_gram(str2, 2, "char")
print("bi-gram")
print(x)
print(y)

X = set(n_gram(str1, 2, "char"))
Y = set(n_gram(str2, 2, "char"))

print("和集合")
print(X|Y)

print("差集合")
print(X - Y)

print("'se'というbi-gramがXおよびYに含まれるかどうか")
print("Xの場合")
print("se" in X)
print("Yの場合")
print("se" in Y)
