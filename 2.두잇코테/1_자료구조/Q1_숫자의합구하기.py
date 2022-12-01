"""
https://www.acmicpc.net/problem/11720
각자리의 수의 합을 구하세요.
"""
n = int(input())
word = list(input())
word = list(map(int, word))
print(sum(word))
