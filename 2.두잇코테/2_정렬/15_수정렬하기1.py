"""
https://www.acmicpc.net/problem/2750
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

시간차이
sort-> 108
n^2 -> 276
"""

n = int(input())
lst = [int(input()) for _ in range(n)]

# lst.sort()
for i in range(n-1):
    for j in range(n-1-i):
        if lst[j]> lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for x in lst:
    print(x)