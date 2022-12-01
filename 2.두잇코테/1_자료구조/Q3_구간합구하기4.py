"""
https://www.acmicpc.net/problem/11659
주어진 구간의 합을 구하세요.

핵심
1. input() 구간을 전부 sys.stdin.readline처리해야됨. -> 안하면 시간초과발생
2. 접근방법 걍 두번째 리스트값을 받을때 미리 계산해놓는다.
3. 요청한 구간에 대해서 값을 꺼내와 처리한다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
sum_list = [0]
num = 0

for i in num_list:
    num += i
    sum_list.append(num)

for i in range(M):
    start, end = map(int, input().split())
    print(sum_list[end] - sum_list[start - 1])