"""
n(2 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다.
각 버스는 한 번 사용할 때 필요한 비용이 있다.
모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
첫째 줄에 도시의 개수 n이 주어지고 둘째 줄에는 버스의 개수 m이 주어진다.

@@@@ 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다. @@@@@@
"""
import sys

n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    graph[a][a] = 0

for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    if c < graph[a][b]:     # 여러개의 노드들 중에서 가장 짧은 값 선택
        graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:          # 도착 불가능이면, 0을 찍어라.
            graph[a][b] = 0
        print(graph[a][b], end=' ')
    print()