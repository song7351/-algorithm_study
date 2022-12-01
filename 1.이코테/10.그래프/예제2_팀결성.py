"""
0번~N번
1. 팀 합치기 연산
2. 특정 2명 학생이 같은 팀 여부 확인 연산

입력
1줄: N, M
M줄: 0/1 a b
0은 합치기 연산
1은 같은 팀 여부 확인 연산

입력값
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""
# 노드정보 입력
n, m = map(int, input().split())

# 부모노드 초기화
parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i

# 같은 팀 확인 연산
def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]

# 합치기 연산
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    d, a, b = map(int, input().split())
    if d == 0:
        # 합치기 연산
        union(parent, a, b)

    elif d == 1:
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")