"""
https://www.acmicpc.net/problem/1546

1. 가장 큰값을 고른다.
2. 모든 점수들을 점수/큰값*100 으로 변환시킨뒤
3. 평균을 새롭게 구하라
"""
n = int(input())
lst = list(map(int, input().split()))
m = max(lst)
lst2 = [x/m*100 for x in lst]
print(sum(lst2)/n)