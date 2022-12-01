"""
편의점 주인 동빈이는 N개의 동전을 가지고있다.
N개의 동전을 이용하여 **만들 수 없는** 양의 정수 금액 중 최솟값은?
1줄: N
2줄: n1 n2 n3 ... N개. ni원
"""

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)