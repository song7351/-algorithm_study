"""
여행지 1~N번

양방향 도로 존재
여행지에 속한 도시의 수 M

접근방법: 서로소 집합
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""
n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

# --------------------------------------------

board = [list(map(int, input().split())) for _ in range(n)]
lst = list(map(int, input().split()))

def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    for j in range(i+1, n):
        if board[i][j] == 1:
            union(parent, i+1, j+1)

for i in range(1,n):
    find(parent, i)

for i in range(m-1):
    if parent[lst[i]] != parent[lst[i+1]]:
        print("NO")
        break
else:
    print("YES")