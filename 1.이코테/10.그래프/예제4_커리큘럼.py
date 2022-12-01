"""
1번 ~ N번까지 강의번호
모든 강의를 수강하는데 걸리는 최소 시간은?

1줄: N
n줄: 강의시간 선수과목

입력
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""

n = int(input())

# 진입차수 계산
indegree = [0]*(n+1)

# 연결정보 초기화
graph = [[] for _ in range(n+1)]

# 강의시간 초기화
time = [0]*(n+1)

# 간선 정보 입력
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    # 강의시간 입력
    time[i] = tmp[0]
    for j in range(1, len(tmp)-1):
        # 부모노드(선수과목)로 설정
        graph[tmp[j]].append(i)
        # 자식노드들이 늘수록 진입차수 +1
        indegree[i] += 1


def topology_sort():
    q = []
    result = time[:]

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.pop(0)

        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], time[i] + result[now])
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()