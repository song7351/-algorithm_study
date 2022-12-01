"""
0,0 -> N-1,N-1
이게 다익스트라도 아니고 bfs에 조건설치한듯 합니다.
시작점 0,0에서 상하좌우 이동시
기존의 기록된 값보다 적은 비용일때만 waiting 리스트에 담아서 계속 이동 시킨다.
"""
t = int(input())
INF = int(1e9)
for _ in range(t):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    memo = [[INF]*n for _ in range(n)]
    memo[0][0] = board[0][0]

    waiting = [(0,0)]

    while waiting:
        x,y = waiting.pop(0)
        for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
            ni = x + di
            nj = y + dj
            if 0<= ni < n and 0<= nj < n:
                if memo[ni][nj] > memo[x][y] + board[ni][nj]:
                    memo[ni][nj] = memo[x][y] + board[ni][nj]
                    waiting.append((ni,nj))
    print(memo[n-1][n-1])