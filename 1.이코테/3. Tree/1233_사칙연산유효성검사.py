"""
첫 줄에는 각 케이스의 트리가 갖는 정점의 총 수 N(1≤N≤200)이 주어진다.
test_case = 10
정점 번호, 정점정보, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호

트리는 완전 이진 트리 형식

(단, 계산이 가능한지가 아닌 유효성을 검사하는 문제이므로 0으로 나누는 경우는 고려하지 않는다. )
계산이 불가능한 경우
1. 부모가 숫자일때, 밑에 자식이 있는경우
2. 부모가 사칙연산일때, 밑에 자식이 2개가 아닌경우
3. 부모가 사칙연산일때, 자식이 사칙연산인 경우
"""
import sys; sys.stdin = open('1233_사칙연산유효성검사.txt')

def check(n):
    if n <= N:
        c1 = check(2*n)
        c2 = check(2*n + 1)
        if c1 is None:      # 마지막줄 노드를 의미
            return par[n]
        elif c2 is None:    # 자식이 하나만 있으면 유효성 실패
            par[n] = False
            return par[n]
        if c1 in ['+','-','*','/',False] or c2 in ['+','-','*','/',False]:  # 자식중 하나라도 사칙연산 혹은 False이면 실패
            par[n] = False
            return par[n]
        if par[n] in ['+','-','*','/']: # 자식들이 전부 숫자이고 부모가 사칙연산이면 성공
            par[n] = True
            return par[n]
        else:                           # 자식들이 전부 숫자이지만 부모가 숫자라면 실패
            par[n] = False
            return par[n]

test_case = 10

for tc in range(1, test_case + 1):
    N = int(input())
    par = [0] * (N+1)

    for _ in range(N):
        lst = list(input().split())
        if lst[1].isdigit():
            par[int(lst[0])] = int(lst[1])
        else:
            par[int(lst[0])] = lst[1]

    ans = check(1)
    if ans:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')