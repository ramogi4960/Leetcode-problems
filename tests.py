from collections import Counter
x = [1, 2, 5, 7, 5, 7, 2, 9, 8, 9, 3, 5, 1, 2]
name = "lruthcgnushmshuxtbrgbcnermxbnu"
for item in Counter(name).items():
    print(f"{item[0]} : {item[1]}")