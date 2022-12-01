"""
https://www.acmicpc.net/problem/18406

현재 캐릭터의 점수를 N이라고 할 때,
필살기: N을 자릿수를 기준으로 반으로 나누어 왼쪽 각합 과 오른쪽 각합이 동일한 상황

필살기 사용이 가능하다면 LUCKY
아니라면, READY
N은 항상  짝수 자리이다.
"""
N = list(map(int, input()))
n = len(N)
sum_a = 0

for i in range(n//2):           # 왼쪽의 합만 구한다.
    sum_a += N[i]

if sum(N)-sum_a == sum_a:       # 전체합-왼쪽합 == 오른쪽합 == 왼쪽합
    print('LUCKY')
else:
    print('READY')