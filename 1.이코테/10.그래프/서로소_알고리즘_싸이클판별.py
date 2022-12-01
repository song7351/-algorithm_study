"""
기본 원리.
서로소 알고리즘과 동일하다. 그러나 입력받을때마다, 부모노드가 동일한지 체크한다.
동일하다면 싸이클 이라고 판단한다.

작업순서.
1. 노드 정보 입력받기
2. 부모테이블 초기화
3. Union 연산
    3-1. 각 노드의 루트노드 찾는 find 연산
        3-1-1. 만약 각 루트노드가 동일하다면 싸이클 판단!
    3-2. 부모노드 설정
    3-3. 집합 합치기

4. 전체 find연산 재실행: 그룹으로 완전히 쪼개기 위해서.

입력값
3 3
1 2
1 3
2 3
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

cycle = False
# 3. Union 연산
for i in range(e):
    a,b =  map(int, input().split())
    # 3-1-1. 싸이클 판단
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    union_parent(parent, a, b)
if cycle:
    print("싸이클 형성!")
else:
    print(f"Union연삭 직후: {parent[1:]}" )
    # 4. 한번 전체 부모노드 정리
    for i in range(1, v+1):
        find_parent(parent, i)

    print(f"전체 find연산 직후: {parent[1:]}")
