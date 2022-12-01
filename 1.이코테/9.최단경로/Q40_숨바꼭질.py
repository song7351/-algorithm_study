"""
1~N번방 중에 숨는다.
술래는 1번부터 검사한다.
전체 맵에는 총 M개의 양방향 통로가 존재

출력
1번값: 최단거리 헛간중 가장 먼 헛간 번호
단, 동일거리는 가작 작은 번호를 출력
2번값: 해당 거리값
3번값: 해당 거리값을 가진 헛간의 수
"""

n,m = map(int, input().split())

INF = int(1e9)
graph = [[INF]*n for _ in range(n)]

# 본인 헛간 가는 경우 초기화
for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    # 양방향 통로 설정
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans2 = max(graph[0])
ans1, ans3 = 0, 0
for i in range(n):
    if graph[0][i] == ans2:
        ans3 += 1
        if ans1 == 0:
            ans1 = i+1

print(ans1, ans2, ans3)