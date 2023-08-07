from itertools import permutations as pm
x = ["cats", "dog", "sand", "and", "cat"]
y = "catsandog"
for i in range(1, len(x) + 1):
    for item in pm(x, i):
        try:
            if item[0] == 'cats' and item[1] == 'and' and item[2] == 'dog':
                print(''.join(item))
        except:
            pass
