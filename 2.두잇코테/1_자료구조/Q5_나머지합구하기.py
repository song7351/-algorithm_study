"""
https://www.acmicpc.net/problem/10986

접근방법
- 기본 접근방식은 구간합구하기4랑 동일
- 그러나, 합의 나머지를 값으로 넣는다.
- 그러면 0 ~ m-1값들이 나오는데 여기서 구간합구하기4처럼 해당 구간을 구하는데
- 나머지들끼리 마이너스했을때 0이 나오면 m의 배수라는 뜻
- 나머지들끼리 마이너스했을때 0이 나오려면 값이 같다는 뜻.
- 그러면 0 ~ m-1값들이 각각 몇개인지 구해서
- 그 개수에서 무작위로 2개를 뽑는 경우의 합이 정답이다.
- 추가로 애초에 0이 나온 낱개는 m의 배수이므로 기본 정답 수이다.

--------------------------------------
테스트 케이스 예시
        5 3
        1 2 3 1 2
        1 3 6 7 9
lst     1 0 0 1 0
lst2    3 2 0
"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst2 = [0]*m
tmp = 0
for i in range(n):
    tmp += lst[i]
    lst2[tmp%m] += 1

ans = lst2[0]
for i in range(m):
    if lst2[i] >= 2:
        ans += lst2[i] * (lst2[i]-1) // 2

print(ans)