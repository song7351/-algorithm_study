"""
N*N 크기의 복도
각 선생님들은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시
복도에 장애물이 위치한 경우, 선생님은 장애물 뒤편에 숨어 있는 학생들은 볼 수 없다.
장애물로 막히기 전까지의 학생들은 모두 볼 수 있다

정확히 3개의 장애물을 설치해야 한다
목표: 모든 학생들이 감시에서 벗어남.

X, S, T : 공백, 학생, 선생
"""
import sys
from itertools import combinations
N = int(input())
board = [list(sys.stdin.readline().split()) for _ in range(N)]
X_list = []     # 공백 리스트
T_list = []     # 학생 리스트
S_list = []     # 선생 리스트
for i in range(N):
    for j in range(N):
        if board[i][j] == 'X':
            X_list.append([i,j])
        elif board[i][j] == 'T':
            T_list.append([i,j])
        else:
            S_list.append([i,j])

O_list = list(combinations(X_list,3))   # 공백리스트에서 3개를 골라서 벽리스트를 만든다.
di = [-1,1,0,0]
dj = [0,0,-1,1]

ans = 'NO'
for target_O in O_list:
    new_board = [item[:] for item in board]
    for x,y in target_O:        # 벽설치
        new_board[x][y] = 'O'

    flag = 0
    pass_cnt = 0
    for tx,ty in T_list:            # 선생리스트중 1명 뽑음
        cnt = 0                     # 4방향을 체크하는 용도
        for k in range(4):
            L = 1
            while True:             # 설정한 방향으로 쭉쭉 검사함.
                ni = tx + di[k]*L
                nj = ty + dj[k]*L
                if 0<= ni < N and 0<= nj < N:
                    if new_board[ni][nj] == 'S':    # 검사결과 학생이 나오면 전체에서 다음 벽설치로 넘어감
                        flag = 1                    # 다음 벽설치로 넘어가기 위한 변수
                        break
                    elif new_board[ni][nj] == 'O':  # 만약 학생이 안나오고 쭉쭉가서 벽이나온다면? -> 해당 방향은 문제 없음
                        cnt += 1
                        break
                else:                               # 만약 학생이 안나오고 쭉쭉가서 범위를 벗어나면? -> 해당 방향은 문제없음
                    cnt += 1
                    break
                L += 1
            if cnt == 4:                            # 4방향 문제 없다면,
                pass_cnt += 1                       # 해당 선생님은 통과 1스택
            if flag == 1:                           # 별개로, 만약 학생이 나왔다면 다음 벽설치까지 break
                break
        if flag == 1:
            break
    if flag == 1:
        continue
    if pass_cnt == len(T_list):                     # 선생님 통과 stack이 선생님 리스트 길이와 같다면?
        ans = "YES"                                 # 성공.
        break

print(ans)