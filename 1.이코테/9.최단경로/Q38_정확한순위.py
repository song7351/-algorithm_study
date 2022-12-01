"""
정확하게 순위를 알 수 있는 학생의 수는?

1줄: N M 학생수, 성정 비교횟수
M줄: a < b a번학생 < b번학생

수평으로 결과검색
1. 행번호(고정) -> 열번호 검색시 INF가 1개있다면, 갈 수 없는 노드가 1개라는 뜻이고 이는 n-1등 이라는 뜻이다.

수직으로 결과검색
2. 행번호 -> 열번호(고정) 검색시 INF가 1개있다면, 한 개의 노드만 해당 열번호 노드로 갈 수 없으므로 최초의 1등에서 1+1등이라는 뜻이다.

수평, 수직으로 검사 결과 등수가 서로 같다면 등수 확정.
다를경우 해당 등수들중 하나이다.
"""
n,m = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a,b= map(int, input().split())
    # a에서 b가는데 c비용
    graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # a->b 가는값은 a->b 가는값, a->k->b 가는값 중 최소값.
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

ans = 0
for i in range(1,n+1):
    Vcnt = 1
    Hcnt = n
    for j in range(1, n+1):
        if graph[i][j] == INF:
            Hcnt -= 1
        if graph[j][i] == INF:
            Vcnt += 1
    if Hcnt == Vcnt:
        ans += 1

print(ans)
