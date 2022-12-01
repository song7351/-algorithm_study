"""
모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우
기본적으로 다익스트라랑 비슷하지만
매 단계마다 최단 거리를 갖는 노드를 찾지 않는다.
기본적으로 방문기록을 2차원 배열에 저장하므로 해당 기록을 N번 반복하기때문에
복잡도는 N**3이다.

1. 단순히 1번 노드를 거쳐 가는 경우를 고려
2. 다른 경로를 걸쳐 이동한 경우와 1번 노드를 거쳐 이동한 경우를 비교.
3. ...
"""

INF = int(1e9)

n = int(input())
m = int(input())

# 이동 기록을 남길 2차원 리스트
graph = [[INF]*(n+1) for _ in range(n+1)]

# 본인 노드에서 본인 노드이동은 비용이 0이다.
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int, input().split())
    # a에서 b가는데 c비용
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # a->b 가는값은 a->b 가는값, a->k->b 가는값 중 최소값.
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
