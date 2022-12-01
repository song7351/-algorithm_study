"""
상하좌우
N * N 크기의 공간
가장 왼쪽위의 좌표는 1,1
가장 오른쪽 아래는 N,N
시작좌표 1,1 고정에서
상하좌우 이동이 가능하다.
L R U D 명령을 통해 최종 도착하는 좌표는?
"""

N = int(input())    # 공간의 크기
lst = list(input().split())   # LRUD 명령

board = [[0]* N for _ in range(N)]      # 총 공간의 크기
di = [-1,1,0,0]
dj = [0,0,-1,1]                         # 상하좌우
d = ['U','D','L','R']
x,y = 0,0                               # 시작지점 (0,0)
for i in lst:
    for j in range(4):
        if i == d[j]:
            ni = x + di[j]
            nj = y + dj[j]
            if 0<= ni < N and 0<= nj < N:
                x,y = ni,nj

print(x+1, y+1)                         # 문제에서 시작지점은 (1,1)