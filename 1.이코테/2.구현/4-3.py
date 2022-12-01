"""
왕실의 나이트
체스판 = 8 * 8
나이트 이동
방법1. 수평으로 두칸이동후 수직으로 한칸이동
방법2. 수직으로 두칸이동후 수평으로 한칸이동
행 1~8
열 a~h
"""

point = list(input())
row = int(point[1]) -1          # 행 index 구하기 (0~n-1)
cols = ['a','b','c','d','e','f','h']
col = 0
for i in range(8):              # 열 index 구하기 (0~n-1)
    if point[0] == cols[i]:
        col = i
        break

board = [[0]*8 for _ in range(8)]
# 상2좌우, 하2좌우, 좌2상하, 우2상하
di = [2,2,-2,-2,1,-1,1,-1]
dj = [-1,1,-1,1,-2,-2,2,2]
cnt = 0

for i in range(8):                  # 이동가능한 8개 전부 검사.
    ni = row + di[i]
    nj = col + dj[i]
    if 0<= ni < 8 and 0<= nj < 8:
        cnt += 1

print(cnt)