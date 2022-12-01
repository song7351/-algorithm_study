test_case = int(input())

def check(i,n,ac,lc):
    global ans_cnt, len_cnt
    if i == n:
        if ac > ans_cnt:
            len_cnt = lc
        elif ac == ans_cnt:
            if len_cnt > lc:
                len_cnt = lc
    else:
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            k = 1
            tmp = []
            while k < N:
                ni = core_lst[i][0] + di*k
                nj = core_lst[i][1] + dj*k
                k += 1
                if 0<= ni < N and 0<= nj < N:
                    if board[ni][nj] == 0:
                        tmp.append((ni,nj))
                    else:
                        check(i+1, n, ac, lc)
                        break
            else:
                ac += 1
                for x,y in tmp:
                    lc += 1
                    board[x][y] = 3
                check(i+1, n, ac, lc)
                ac -= 1
                for x,y in tmp:
                    lc -= 1
                    board[x][y] = 0

for tc in range(1, test_case+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    ans_cnt = 0
    len_cnt = 0
    core_lst = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                if i == 0 or j == 0 or i == N-1 or j == N-1:
                    ans_cnt += 1
                else:
                    core_lst.append((i,j))
    check(0,len(core_lst),ans_cnt,len_cnt)
    print(f"#{tc} {len_cnt}")