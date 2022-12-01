import sys

def dijkstra(N):
    d = [[INF]*N for _ in range(N)]
    u = [[0]*N for _ in range(N)]
    d[0][0] = board[0][0]

    for _ in range(N**N):
        wi,wj = 0,0
        minV = INF
        for i in range(N):
            for j in range(N):
                if u[i][j] == 0 and minV > d[i][j]:
                    minV = d[i][j]
                    wi,wj = i,j
        u[wi][wj] = 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            vi, vj = wi+di, wj+dj
            if 0<= vi<N and 0<= vj<N:
                d[vi][vj] = min(d[vi][vj], d[wi][wj]+board[vi][vj])

    return d[N-1][N-1]
INF = int(1e9)
tc = 1
while True:
    N = int(input())
    if N == 0:
        break
    board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    print(f"problem {tc}: {dijkstra(N)}")
    tc += 1