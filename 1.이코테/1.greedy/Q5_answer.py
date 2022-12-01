"""
A,B 두사람이 볼링을 친다.
볼링은 총 N개.(1번부터 N번)
무게는 1~M
두사람은 서로 다른 무게의 볼링공을 선택한다.

1줄: N M
2줄: m1 m2 m3 m4 m5.... N개 mi는 무게

원리: 경우의 수
서로 다른 무게의 볼링공을 선택한다 == 같은무게 공을 빼고 나머지 다른 공의 수 * 같은무게 공
"""

N,M = map(int,input().split())
gong = list(map(int, input().split()))

gong_cnt = [0] * 11
ans = 0
for i in gong:
    gong_cnt[i] += 1

for i in gong_cnt:
    N = N-i
    ans += N * i

print(ans)
