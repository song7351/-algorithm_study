"""
마을 N개  연결 M개의 길(양방향)
2개의 집단
전체 유지비 가장 작은 경우는?

1줄: N, M
M줄: a,b, cost

접근방법
2개의 최소신장 트리를 가진다 (x)
1개의 최소신장 트리에서 가장 큰 연결값을 가진 선을 지우면,
2개의 신장 트리가 나온다.

입력값
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""
# 노드 정보를 받는다.
n, m = map(int, input().split())

# 부모노드 저장소
parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i

# 비용 정보를 받는다.
edges = []
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

# 최소비용 정렬
edges.sort()

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

result = []
for edge in edges:
    cost, a, b = edge

    # 서클인지 확인
    if find(parent, a) != find(parent, b):
        result.append(cost)
        union(parent, a, b)

print(sum(result) - result[-1])