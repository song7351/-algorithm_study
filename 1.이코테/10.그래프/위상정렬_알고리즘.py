"""
사전지식
진입차수: 해당 노드에 들어오는 간선의 개수

위상정렬
정의: 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'

기본원리
- 진입차수가 0인 노드를 큐에 넣는다.
- 큐가 빌때 까지 아래 과정을 반복
    - 큐에서 원소를 꺼내서 해당 노드에서 출발하는 간선을 그래프에서 제거
    - 새롭게 진입차수가 0인 노드를 큐에 넣는다.
@@@ 특징: 정답이 여러개 일 수 있다.

입력값
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""

from collections import deque

# 1. 노드 정보를 입력받는다.
v, e = map(int, input().split())

# 2. 진입차수 기록 초기화
indegree = [0]*(v+1)

# 3. 노드 연결 그래프 초기화
graph = [[] for i in range(v+1)]

# 4. 노드 연결 및 진입차수 계산
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

print(graph)
# 5.. 위상 정렬 함수
def topology_sort():
    result = [] # 출력할 결과 리스트
    q = deque()

    # 최초에 진입차수가 0인 함수를 q 리스트에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 진입차수가 0인 노드 pop
        now = q.popleft()
        # 출력할 결과에 append
        result.append(now)

        # 진입차수가 0인 노드와 연결된 다른 노드들의 차수 -1
        for i in graph[now]:
            indegree[i] -= 1
            # 근데 만약 해당 차수가 0이면 q에 append
            if indegree[i] == 0:
                q.append(i)

    # 결과값 출력
    print(*result)

topology_sort()