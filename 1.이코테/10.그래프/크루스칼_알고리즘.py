"""
신장트리
정의: 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
간단: 사이클이 없는 모든 노드가 연결된 그래프

1. 크루스칼 알고리즘
-> "최소" 신장 트리
-> 시간복잡도는 NlogN6

기본 원리
- 모든 간선의 비용을 오름차순 정렬한다.
- 하나씩 선택한다.
- 사이클인지 확인한다.
- 반복.

작업순서
작업순서.
1. 노드 정보 입력받기
2. 부모테이블 초기화
3. 비용 정보 입력받기
4. 비용 정보 오름차순 정렬
5. 작업시작
 5-1. 사이클 확인
 5-2. Union 연산
 5-3. find 연산

6. 출력

입력값
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""
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

# 1. 노드 정보 입력받기
v,e = map(int, input().split())

# 2. 부모테이블 초기화
parent = [0]*(v+1)

for i in range(v+1):
    parent[i] = i

# 3. 비용테이블 입력받기
edges = []  # (비용, 노드1, 노드2) 모든 연결 정보가 들어갈 리스트
result = 0

for _ in range(e):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

# 4. 비용 오름차순 정렬
edges.sort()

# 5. 작업시작
for edge in edges:
    cost, a, b = edge
    # 5-1. 사이클 검사
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)