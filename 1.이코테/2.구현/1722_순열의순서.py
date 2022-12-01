"""
https://www.acmicpc.net/problem/1722
1줄: N -> N! 순열조합
"""
import sys
input = sys.stdin.readline

def find_lst(i, N):
    global cnt, ans
    if i == N:
        cnt += 1
        if cnt == board[0]:
            ans = lst[:]
    else:
        if cnt == board[0]:
            return
        for j in range(i, N):
            lst[i], lst[j] = lst[j], lst[i]
            find_lst(i+1, N)
            lst[i], lst[j] = lst[j], lst[i]

def find_idx(i, N):
    global cnt, ans
    if i == N:
        cnt += 1
        if lst[:] == board:
            ans = cnt
            return
    else:
        if ans and ans == cnt:
            return
        for j in range(i, N):
            lst[i], lst[j] = lst[j], lst[i]
            find_idx(i+1, N)
            lst[i], lst[j] = lst[j], lst[i]

n = int(input())
lst = [i for i in range(1,n+1)]
board = list(map(int,input().split()))
x = board.pop(0)
cnt = 0
ans = 0
if x == 1:
    find_lst(0, n)
    ans = map(str, ans)
    print(' '.join(ans))
else:
    find_idx(0,n)
    print(ans)

