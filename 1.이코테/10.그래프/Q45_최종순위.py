"""
1~n번 팀
놀랍게도 올해 참가한 팀은 작년에 참가한 팀과 동일하다!
작년에 비해서 성적 순위가 바뀐 팀 목록만 발표한다.

접근방법
그래프 + 순서??? == 위상정렬
"""

test_case = int(input())
for _ in range(test_case):
    n = int(input())                        # 팀 수
    lst1 = list(map(int, input().split()))  # 작년 등수

    indegree = [0]*(n+1)                    # 진입차수
    graph = [[0]*(n+1) for _ in range(n+1)] # 그래프 설정
    for i in range(n):                      # 높은 등수에서 낮은 등수로 이동하는것을 기록하겠다.
        for j in range(i+1, n):             # 왜냐? 마지막에 프린트 편하라고...
            graph[lst1[i]][lst1[j]] = 1
            indegree[lst1[j]] += 1

    m = int(input())                        # 상대적 등수가 바뀐 수
    for _ in range(m):
        a,b = map(int, input().split())
        if graph[a][b] == 1:
            graph[a][b] = 0
            graph[b][a] = 1
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = 1
            graph[b][a] = 0
            indegree[a] -= 1
            indegree[b] += 1

    q = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    cycle = False
    error = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            error = True
            break
        now = q.pop(0)
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif error:
        print("?")
    else:
        print(*result)

