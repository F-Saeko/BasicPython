text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
words = text.replace(",","").replace(".","").split()
文字数 = list(map(len,words))

print(''.join(map(str,文字数)))