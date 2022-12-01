"""
메세지 전달을 위해서는 양방향으로 연결되어있어야한다.
C에서 모든 도시로 메세지를 전달하려한다.
총 몇개의 도시가 전달받고 총 소요 시간은?
도시N 통로M개 시작C
"""

N,M,C = map(int, input().split())
INF = int(1e9)

start = C
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [INF] * (N+1)

for _ in range(M):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(N-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)
cnt_city = 0
max_distance = 0

for i in range(1, N+1):
    if i != start and distance[i] != INF:
        cnt_city += 1
        if distance[i] > max_distance:
            max_distance = distance[i]

print(cnt_city, max_distance)