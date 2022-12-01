"""
N개의 집(0번~N-1번)
M개의 도록

최소비용 - 최대절약금액
접근방법: 크루스칼

7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
"""
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i

lst = []
for _ in range(m):
    a,b,c = map(int, input().split())
    lst.append((c,a,b))
lst.sort()

answer = 0
for tmp in lst:
    c,a,b = tmp
    answer += c
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer -= c

print(answer)