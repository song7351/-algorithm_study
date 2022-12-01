"""
N×N크기의 땅
1줄: N,L,R
N줄: 국가,인구정보

국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
연합을 해체하고, 모든 국경선을 닫는다.
"""
import sys
# sys.setrecursionlimit(10**6)

N,L,R = map(int,input().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

di = [-1,1,0,0]
dj = [0,0,-1,1]
ans = 0

def bfs(i,j):
    waited = [(i,j)]
    grp = [(i,j)]
    while waited:
        x,y = waited.pop(0)
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0<= ni < N and 0<= nj < N:
                if L <= abs(board[x][y] - board[ni][nj]) <= R:
                    if (ni,nj) not in visited:
                        visited.append((ni,nj))
                        waited.append((ni,nj))
                        grp.append((ni,nj))
    return grp

while True:
    visited = []
    grps = []
    for i in range(N):
        for j in range(N):
            if (i,j) not in visited:
                visited.append((i,j))
                small_grp = bfs(i,j)
                grps.append(small_grp)

    if len(grps) == N**2:
        break
    else:
        ans += 1

    for sgrp in grps:
        s = 0
        n = len(sgrp)
        for x,y in sgrp:
            s += board[x][y]

        for x,y in sgrp:
            board[x][y] = s//n

print(ans)