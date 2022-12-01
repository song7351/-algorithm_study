"""
0,0 -> N-1,N-1
상하좌우 이동
"""
t = int(input())
INF = int(1e9)
for _ in range(t):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    memo = [[INF] * n for _ in range(n)]
    memo[0][0] = board[0][0]

    for i in range(1, n):
        memo[0][i] = board[0][i] + memo[0][i - 1]
        memo[i][0] = board[i][0] + memo[i - 1][0]

    for i in range(1, n):
        for j in range(1, n):
            memo[i][j] = min(memo[i - 1][j], memo[i][j - 1]) + board[i][j]

    print(memo[n - 1][n - 1])