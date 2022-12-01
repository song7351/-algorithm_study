lst1 = list(input())
lst2 = list(input())
n,m = len(lst1), len(lst2)
memo = [-1]*n
v = -1
for i in range(n):
    for j in range(m):
        if lst1[i] == lst2[j] and j > v:
            memo[i] = j
            v = j
            break

cnt = 0
for i in memo:
    if i != -1:
        cnt += 1

print(m-cnt)