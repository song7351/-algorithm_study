"""
https://www.acmicpc.net/problem/3109

"""
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
board2 = [[0]*c for _ in range(r)]

for i in range(r):
    board2[i][0] = 1

for i in range(0, c-1):
    for j in range(r):
        if board[j][i] != 'x' and board2[j][i] != 0:
            if j == 0:
                if board[j][i+1] !='x':
                    board2[j][i+1] += 1
                if board[j+1][i+1] != 'x':
                    board2[j+1][i+1] += 1

            elif j == r-1:
                if board[j-1][i+1] != 'x':
                    board2[j-1][i+1] += 1
                if board[j][i+1] !='x':
                    board2[j][i+1] += 1

            else:
                if board[j-1][i+1] != 'x':
                    board2[j-1][i+1] += 1
                if board[j][i+1] != 'x':
                    board2[j][i+1] += 1
                if board[j + 1][i+1] != 'x':
                    board2[j+1][i+1] += 1

cnt = int(1e9)
cnt_lst = []
for i in range(1,c):
    tmp = 0
    tmp_lst = []
    for j in range(r):
        if board2[j][i] != 0:
            tmp += 1
            tmp_lst.append(board2[j][i])
    if tmp < cnt:
        cnt = tmp
        cnt_lst = tmp_lst

ans = set(cnt_lst)

for x in board2:
    print(x)

print(ans)
print(len(ans))