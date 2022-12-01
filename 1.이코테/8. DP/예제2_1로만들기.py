"""
정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
1. X가 5로 나누어떨어지면 5로 나눈다.
2. 3으로 ~ 3으로 ~
3. 2로 ~ 2로
4. X에서 1을 뺀다.

목표: 연산 4개를 적당히 사용해서 1을 만든다. 연산 사용횟수의 최솟값은?
1<= N <= 30,000
원래는 어떻게 구할것인가?
- 5,3,2 순으로 나눌 수 있나? -> 없다면 1을 빼라.
- 5,3,2 순으로 나눌 수 있나? -> 없다면 1을 빼라.
- 결국 전부 나누면 마지막엔 1이 남음.

우리는 어떻게 구할것인가?
해당 인덱스를 X라 본다. 그때 최소값을 기록한다. 어떻게?
만약 X가 5,3,2의 배수라면 현재 상태에서 1회 계산하면 5,3,2의 이전 배수카운트가 된다.
즉 만약 X가 9라면 X가 3일때 최소값에 + 1회 계산하면 최소값이 나온다.
그러면 X가 만약 90이라면? -> 45에서의 최소값, 30에서의 최소값, 18에서의 최소값들 중 최소값을 입력하면된다.

기본적인 인덱스 X의 1증가는 4번 연산으로 보고 이전 횟수에서 1을더한다.
기본적인 값과 위에서 배수일때중 최소값을 값으로 설정한다.
"""

N = int(input())

memo = [0]*30001

for i in range(2,N+1):
    memo[i] = memo[i-1] + 1

    if i%2 == 0:
        memo[i] = min(memo[i], memo[i//2] + 1)
    if i%3 == 0:
        memo[i] = min(memo[i], memo[i//3] + 1)
    if i%5 == 0:
        memo[i] = min(memo[i], memo[i//5] + 1)

print(memo[N])