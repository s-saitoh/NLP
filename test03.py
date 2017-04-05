#coding: utf-8
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
text = text.replace(".", "")
text = text.replace(",", "")
text = text.split()
num_char = [len(x) for x in text]
print(text)
print(num_char)
