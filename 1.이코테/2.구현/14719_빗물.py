"""
https://www.acmicpc.net/problem/14719

1줄: N M
각줄의 1과 1사이의 0의 개수를 구하면된다.
"""

N, M = map(int, input().split())
board = [[0]*M for _ in range(N)]
lst = list(map(int,input().split()))
for i in range(M):
    for j in range(lst[i]):
        board[j][i] = 1
print(board)
ans = 0
for i in range(N):
    cnt = 0
    flag = 0
    for j in range(M):
        if board[i][j] == 0:
            cnt += 1
        elif board[i][j] == 1 and flag == 1:    # 두번째 나오는 1부터는 0의 개수 cnt를 더해주고 초기화
            ans += cnt
            cnt = 0
        else:                                   # 최초의 1은 시작의 의미에서 flag, cnt는 초기화
            flag = 1
            cnt = 0

print(ans)