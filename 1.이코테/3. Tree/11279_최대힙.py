"""
배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 자연수는 231보다 작다.
"""
import sys

def enque(n):
    global last
    last += 1
    lst[last] = n
    c = last
    p = c//2
    while p and lst[c] > lst[p]:
        lst[p], lst[c] = lst[c],lst[p]
        c = p
        p = c//2

def deque():
    global last
    tmp = lst[1]
    lst[1] = lst[last]
    last -= 1
    if last <= 0:
        last = 0
    p = 1
    c = p * 2
    while c <= last:
        if c + 1 <= last and lst[c] < lst[c + 1]:  # 오른쪽 자식도 있고, 오른쪽자식이 더 크면
            c += 1
        if lst[p] < lst[c]:
            lst[p], lst[c] = lst[c], lst[p]
            p = c
            c = p * 2
        else:
            break
    return tmp

N = int(sys.stdin.readline())
lst = [0] * (100000+1)
last = 0
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        enque(x)
    else:
        if not last:
            print('0')
        else:
            print(deque())