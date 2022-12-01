"""
모험가 N명이 있다.
모험가는 공포수치 X를 가진다.
공포수치가 X인 경우, 모험가는 반드시 X명이상으로 그룹을 만들어야 한다.
**최대** 몇개의 그룹이 만들어 지는가?
단, 모든 모험가가 모험을 떠날 필요는 없다.

입력
1줄: N
2줄: x1 x2 x3 x4 .... N개
"""
''

N = int(input())
gongfo = list(map(int, input().split()))
gongfo.sort()                   # 오름차순 정리
grp_cnt = 0

grp = []
for i in range(N):
    grp.append(gongfo[i])       # 모험가 그룹
    if len(grp) == max(grp):    # 모험가 그룹의 최대공포도 == 그룹인원수
        grp_cnt += 1
        grp = []

print(grp_cnt)
