"""
양방향 도시 1번~ N번 도시
1번도시에서 출발하여 K번도시를 경유하여 X번 도시에 도착하는 최단거리는?
만약 X번 회사에 도착할 수 없다면 -1을 출력하라
1<= N,M,K <= 100
"""
INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]

for a in range(1, N+1):
    graph[a][a] = 0

for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = 1
    # 양방향
    graph[b][a] = 1

# print(graph)

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

X, K = map(int, input().split())

if graph[K][X] == INF:
    print(-1)
else:
    print(graph[1][K] + graph[K][X])