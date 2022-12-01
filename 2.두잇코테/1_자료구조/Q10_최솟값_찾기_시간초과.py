"""
https://www.acmicpc.net/problem/11003
n, l
n개수의수중
di = ai-l+1 ~ ai중 최솟값
d에 저장된 수를 출력하시오.
단, i<=0인 ai는 무시하고 d를 구해라.

46% 시간초과
"""
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
lst = list(map(int, input().split()))

minV = int(1e9)
for i in range(l):
    if lst[i] < minV:
        minV = lst[i]
    print(minV, end=" ")

s = 0
for i in range(l, n):
    if lst[s] == minV:
        minV = min(lst[s+1:i+1])
    if lst[i] < minV:
        minV = lst[i]
    s += 1
    print(minV, end=" ")
