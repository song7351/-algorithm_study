"""
90도씩 돌린 결과를 넣어라.
"""
test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    board = [list(map(str, input().split())) for _ in range(N)]
    print(f"#{tc}")

    for i in range(N):
        n1, n2, n3 = '', '', ''
        for j in range(N):
            n1 += board[N-1-j][i]
            n2 += board[N-1-i][N-1-j]
            n3 += board[j][N-1-i]
        print(n1, n2, n3)