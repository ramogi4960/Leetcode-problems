from itertools import permutations
a = [1, 2, 3]
print(*list(permutations(a, len(a))), sep='\n')
