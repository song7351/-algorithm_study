"""
게임개발
게임 맵크기는 (N * M), 맵종류는 바다, 땅이다.
캐릭터의 현재좌표는 (A,B)
바다는 이동불가능.
이동은 상하좌우.

매뉴얼
1. 현재방향기준으로 반시계방향순으로 탐색
2. 반시계방향 회전후 앞으로 이동가능하면, 이동. 아니면, 다시 1번 실행.
3. 만약 4방향 모두 **가본 칸** 이거나 바다라면,
3-1. 바라보는 방향을 유지한채 뒤로 이동하고 다시 1번 실행
3-2. 뒤쪽이 바다라면, stop

방향: 0123 북동남서
맵종류: 01 육지,바다
"""

N, M = map(int, input().split())    # 열크기, 행크기
y,x,d = map(int, input().split())   # 행번호, 열번호, 방향

board = [list(map(int, input().split())) for _ in range(N)] # 게임 맵
di = [-1,0,1,0] # 북동남서
dj = [0,1,0,-1]
cnt = 1
check = 0                           # 4에 도달하면 매뉴얼 3실행
board[y][x] = 3                     # 이동했던 길이라면, 3으로 표시(시작점)
while True:                         # 시뮬실행
    d -= 1                          # 시계방향 회전
    if d == -1:                     # 북에서 회전시 서(인덱스 마지막)
        d = 3
    ni = y + di[d]
    nj = x + dj[d]
    if 0<= ni < N and 0<= nj < M:   # 회전한곳이 게임맵 안인가?
        if board[ni][nj] == 0:      # 해당 장소가 육지라면 이동해라
            y,x = ni, nj
            check = 0
            cnt += 1
            board[ni][nj] = 3       
        else:
            check += 1
    else:
        check += 1

    if check == 4:                  # 주변이 이동할 수 없다면,
        d -= 2                      # 뒤로 돌아라.
        if d == -1:
            d = 3
        ni = y + di[d]
        nj = x + dj[d]
        if 0 <= ni < N and 0 <= nj < M: # 뒤에가 이동할 수 있는 길이 있는가?
            if board[ni][nj] == 3:      # 뒤로 이동해라
                y, x = ni, nj
                check = 0
                board[ni][nj] = 3
                d -= 2
                if d < 0:
                    d += 4
            else:                       # 만약 뒤에가 범위밖이거나 바다(1)라면 종료
                break
        else:
            break

print(cnt)