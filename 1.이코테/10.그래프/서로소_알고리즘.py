"""
기본 원리.
각 노드를 부모노드-자식노드로 연결
각각의 노드들의 루트노드들을 찾아서 값을 비교하여 부모노드로 설정한다.

연산 속도는 엄청 크다. 그래서 어느정도 가지치기가 필요하다.
하지만, 코테수준에서는 경로 압축정도만 적용해도 충분!

작업순서.
1. 노드 정보 입력받기
2. 부모테이블 초기화
3. Union 연산
    3-1. 각 노드의 루트노드 찾는 find 연산
    3-2. 부모노드 설정
    3-3. 집합 합치기

4. 전체 find연산 재실행: 그룹으로 완전히 쪼개기 위해서.

입력값
6 4
1 4
2 3
2 4
5 6
"""
# find 연산
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union 연산
def union_parent(parent, a, b):
    # 3-1. find 연산
    # 3-2. 부모노드 설정
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 3-3. 집합 합치기
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 1. 노드 정보 입력받기
v, e = map(int, input().split())

# 2. 부모테이블 초기화
parent = [0]*(v+1)

for i in range(1, v+1):
    parent[i] = i

# 3. Union 연산
for i in range(e):
    a,b =  map(int, input().split())
    union_parent(parent, a, b)

print(f"Union연삭 직후: {parent[1:]}" )
# 4. 한번 전체 부모노드 정리
for i in range(1, v+1):
    find_parent(parent, i)

print(f"전체 find연산 직후: {parent[1:]}")
