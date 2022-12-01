from itertools import permutations, combinations
a = [1,0,0,0]
print(list(set(permutations(a))))
b = (1,0)
print(list(b) + [3])