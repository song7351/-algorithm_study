"""
https://www.acmicpc.net/problem/11660
2차원 구간합구하기

접근방법(dp)
1. 정확히는 0,0부터 모든좌표(i,j)까지 사각형 형태의 합을 (i,j)에 넣어서 만든다.
2. 주어진 구간의 bx,by는 0,0부터 bx,by까지의 사각형 형태의 모든 합이므로
3. 겹치는 부분 ax-1, by // bx, ay-1의 값을 빼준다.
4. 그러나 빼준 두 구간은 ax-1, ay-1부분이 겹치므로 다시 더해준다.
"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
sum_board = [[0] for _ in range(n)]
for i in range(n):
    num = 0
    for j in range(n):
        num += board[i][j]
        sum_board[i].append(num)
#print(sum_board)
for i in range(1,n):
    for j in range(n+1):
        sum_board[i][j] += sum_board[i-1][j]
sum_board = [[0]*(n+1)] + sum_board
#print(sum_board)
for _ in range(m):
    ax,ay,bx,by = map(int, input().split())
    ans = sum_board[bx][by] - sum_board[ax-1][by] - sum_board[bx][ay-1] + sum_board[ax-1][ay-1]
    print(ans)

