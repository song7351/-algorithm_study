"""
미로: N * M
시작점은 0,0 출구는 N-1,M-1
괴물0 길1
미로는 반드시 탈출 가능
탈출까지 최소 이동거리는?
"""
"""
N * M 얼음틀
구멍: 0
칸막이: 1
0상하좌우에 0있으면 한덩어리로 취급
그래서 0덩어리의 총 개수는?
"""
def bfs(x,y):
    global idx
    idx += 1
    for k in range(4):                              # 주변 4방향 검색
        ni = x + di[k]
        nj = y + dj[k]
        if 0<=ni<N and 0<=nj<M:                     # index 범위 안?
            if miro[ni][nj] == 1:                   # 값이 1인가?
                miro[ni][nj] = miro[x][y] + 1       # 현재 값에 + 1
                if [ni,nj] not in lst:              # 대기열에 없는가?
                    lst.append([ni,nj])             # 추가해라
                if ni == N-1 and nj == M-1:         # 목표지점 도달하면 재귀 멈추세요.
                    return

    #for item in miro:
    #    print(item)
    #print()

    # s = lst.pop(0) 이것도 작동하긴 함.
    s = lst[idx]
    bfs(s[0],s[1])

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]

di = [-1,1,0,0]
dj = [0,0,-1,1]

idx = 0
lst = [[0,0]]
bfs(0,0)

print(miro[N-1][M-1])