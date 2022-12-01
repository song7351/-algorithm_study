test_case = int(input())

def f(sx,ex, sy, ey):
    s = 0
    for x in range(sx,ex):
        for y in range(sy, ey):
            s += board[x][y]
    return s

for tc in range(1, test_case+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    ans = int(1e9)
    for i in range(N-1):
        for j in range(N-1):
            s1 = f(0,i+1,0,j+1)
            s2 = f(0,i+1,j+1,N)
            s3 = f(i+1,N,0,j+1)
            s4 = f(i+1,N,j+1,N)
            diff = max(s1,s2,s3,s4) - min(s1,s2,s3,s4)
            if diff < ans:
                ans = diff
    print(f"#{tc} {ans}")