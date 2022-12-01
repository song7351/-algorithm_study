"""
https://www.acmicpc.net/problem/2887

N개의 행성 3차원좌표 2개의 행성 각축 기준 좌표차의 절대값중 가장 작은값
총 N-1개의 터널 모든 행성 연결
접근방법: 크루스칼

최초접근.
완전비교탐색으로 모든 행성을 비교해서 리스트를 만들었습니다.
결과: 시간초과

정답
각 좌표별 리스트를 관리.(행성정보 포함)
각 리스트 최소값부터 무조건 2개를 선택.
위의 완전비교탐색으로 모든 행성의 각축별 거리를 비교할 필요가 없음
무조건 최소값부터 2개를 선택하고 탐색.

"""
import sys
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

n = int(input())

parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i

x = []
y = []
z = []
for i in range(1, n+1):
    a,b,c = map(int, sys.stdin.readline().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))

x.sort()
y.sort()
z.sort()

lst = []
for i in range(n-1):
    lst.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    lst.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    lst.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

lst.sort()

result = 0
for tmp in lst:
    c,a,b = tmp
    if find(parent,a) != find(parent, b):
        result += c
        union(parent, a, b)

print(result)