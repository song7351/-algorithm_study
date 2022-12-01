"""
nm크기 금광
0열부터 실행
이동은 오른쪽 상중하
"""
for _ in range(int(input())):
    n,m = map(int, input().split())
    lst = list(map(int, input().split()))
    board = [[] for _ in range(n)]
    idx = 0
    # 2차원 배열로 변환
    for i in range(n):
        for j in range(m):
            board[i].append(lst[idx])
            idx += 1
    
    # 1열 초기화
    memo = [[0]*m for _ in range(n)]
    for i in range(n):
        memo[i][0] = board[i][0]
    
    # 현재좌표기준 왼쪽 상중하중 최대값 + 현재값
    for j in range(1, m):
        for i in range(n):
            v1,v2,v3 = 0,memo[i][j-1],0
            if i-1 >= 0:
                v1 = memo[i-1][j-1]
            if i+1 < n:
                v3 = memo[i+1][j-1]
            memo[i][j] = max(v1,v2,v3) + board[i][j]
    
    # 마지막 열에서 최대값 출력
    ans = 0
    for i in range(n):
        if ans < memo[i][m-1]:
            ans = memo[i][m-1]
    print(ans)