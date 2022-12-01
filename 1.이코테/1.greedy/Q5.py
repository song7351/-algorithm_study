"""
A,B 두사람이 볼링을 친다.
볼링은 총 N개.(1번부터 N번)
무게는 1~M
두사람은 서로 다른 무게의 볼링공을 선택한다.

1줄: N M
2줄: m1 m2 m3 m4 m5.... N개 mi는 무게
"""

N,M = map(int,input().split())
gong = list(map(int, input().split()))

lst = []

for i in range(N):                                  # 모든 2개를 검색
    for j in range(i+1,N):
        if gong[i] != gong[j] and [i,j] not in lst: # 선택된 2개가 무게가 서로 다르고 기존에 뽑은게 아니라면.
            lst.append([i,j])

print(len(lst))