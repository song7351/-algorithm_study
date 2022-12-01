"""
1이 될 때까지
어떠한 수 N이 1이 될 때까지 2개의 과정중 하나를 반복수행한다.
1. N-1
2. N/K (단, N%K == 0일때만 실행.)

총 몇번의 과정을 실행하는가?
"""

N, K = map(int, input().split())    # 어떤수, 나눌수
cnt = 0

while N > 1:
    if N % K == 0:                  # 조건2
        N = N//K
        cnt += 1
    else:                           # 조건1
        N = N-1
        cnt += 1

print(cnt)