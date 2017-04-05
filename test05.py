#coding: utf-8
def n_gram(char, n, mode = "word"):
    """
    Args:
        char:対象の文字列
        n:Nの値
        mode:単語で区切るなら「word」, 文字で区切るなら「char」.デフォルトはword
    Return:
        n_gram:N-gramで分解した結果
    """
    n_gram = []
    # 単語　or 文字で区切る
    if (mode == "word"):
        chars = char.split()  # 単語で区切る
    if (mode == "char"):
        chars = char.replace(" ", "")  # 文字で区切る

    first_n = n
    while n - 1 < len(chars):
        n_gram.append(chars[n - first_n: n])
        n += 1

    return n_gram

char = "I am an NLPer"
print("単語bi-gram")
words = n_gram(char, 2, "word")
print(words)

print("文字bi-gram")
chars = n_gram(char, 2, "char")
print(chars)
