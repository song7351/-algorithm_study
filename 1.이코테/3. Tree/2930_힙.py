"""
최대 힙
연산1. 1 x = x노드 삽입
연산2. 2   = 최댓값 출력후 삭제
첫줄 = 테스트케이스
2줄 = 연산수
N줄 = 연산
"""
def enque(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def deque():
    global last
    tmp = heap[1]
    heap[1] = heap[last]
    last -= 1
    if last <= 0:
        last = 0
    p = 1
    c = p * 2
    while c <= last:  # 자식이 하나라도 있으면
        if c + 1 <= last and heap[c] < heap[c + 1]:  # 오른쪽 자식도 있고, 오른쪽자식이 더 크면
            c += 1
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:
            break
    return tmp

test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    heap = [0] * 100000
    last = 0
    lst = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{tc}', end=' ')
    for i in range(N):
        if lst[i][0] == 1:
            enque(lst[i][1])
        else:
            if last == 0:
                print('-1', end=' ')
            else:
                print(deque(), end=' ')
    print()