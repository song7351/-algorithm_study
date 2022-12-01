"""
G개의 탑승구(1번부터 G번)
P개의 비행기
i번째 비행기를 1~gi번쨰 탑승구 중 하나에 영구 도킹

순서대로 도킹하는데 도킹할 수 없는 비행기가 나오는 경우 중지
최대한 많은 비행기를 도킹하고자 한다.
최대 몇대 가능?

1줄: G
2줄: P
p줄: 도킹 게이트

가능한 탑승구 범위에서 가장 높은 번호의 탑승구부터 1작은 값의 번호를 확인해나감
==> 옆 번호와 연결시키는 개념

4
3
4
1
1

"""

g = int(input())    # 탑승구 1번~g번
p = int(input())    # 비행기 총 p대
lst = [int(input()) for _ in range(p)]

parent = [i for i in range(g+1)]
print(parent)
def find(parent, x):
    if parent[x] != x:
        parent[x] =  find(parent, parent[x])
    return parent[x]

def union(parent, a,b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

ans = 0
for i in lst:
    if find(parent, i):
        union(parent, i, i-1)
        ans += 1

print(ans)