"""
도시크기 N * N
빈칸: 치킨집2 or 집1
치킨거리=집과 가장 가까운 치킨집거리
도시의 치킨거리 = 모든 치킨거리의 합
치킨집은 최대 M개의 치킨만 생존한다.
첫줄: N M
나머지 = 지도
"""

N, M = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)]
house = []                          # 집 좌표
chicken = []                        # 치킨집 좌표
lst = [[]]                          # 치킨집들 최대 M개선택하는 부분집합
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:        # 집 좌표추가
            house.append([i,j])
        elif board[i][j] == 2:      # 치킨집 좌표추가
            chicken.append([i,j])

for i in chicken:                   # 부분집합 만들기
    n = len(lst)
    for j in range(n):
        a = lst[j] + [i]
        if len(a) <= M:             # 치킨집은 최대 M개만 선택한다.
            lst.append(lst[j] + [i])

ans = 10000000

for i in range(1, len(lst)):        # 0은 빈집합이므로 pass, 부분집합 모음중 1개 선택
    sum_a = 0                       # i번째 부분집합모음에서 **도시의 치킨거리**
    for j in range(len(house)):     # 집 1개 선택
        min_a = 100000000
        for k in range(len(lst[i])):# 치킨집과의 거리중에서 가장 짧은것을 고르는 과정
            x = abs(lst[i][k][0] - house[j][0]) + abs(lst[i][k][1] - house[j][1])
            if x < min_a:           # *치킨거리*를 구한다.
                min_a = x
        sum_a += min_a
    if sum_a < ans:                 #  i번째 **도시의 치킨거리**
        ans = sum_a

print(ans)