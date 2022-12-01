"""
정수 삼각형 최대값 출력하세요.
"""
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
memo = [[0]*n for n in range(1, n+1)]
memo[0][0] = board[0][0]
for i in range(1,n):
    for j in range(i+1):
        v1,v2 = 0,0
        if j-1 >= 0:
            v1 = memo[i-1][j-1]     # 왼쪽위 기록
        if j <= i-1:
            v2 = memo[i-1][j]       # 현재위 기록
        # 2개값중 큰값 + 현재 board값
        memo[i][j] = max(v1,v2) + board[i][j]

print(max(memo[n-1]))