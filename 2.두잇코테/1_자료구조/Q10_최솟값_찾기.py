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
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
lst = list(map(int, input().split()))

minV = int(1e9)

