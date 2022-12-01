"""
부품 N개
손님이 M개 종류의 부품을 대량구매
1줄: N
2줄: Ni ~
3줄: M
4줄: Mi ~
"""
# 이진탐색
def b_search(start, end, target):
    if start <= end:
        middle = (start+end)//2
        if N_lst[middle] == target:
            print('yes', end=' ')
            return
        elif N_lst[middle] > target:
            b_search(start, middle-1, target)
        else:
            b_search(middle+1,end,target)
    else:
        print('no', end=' ')    # 결국 타겟을 못찾으면 start>end 까지 진행됨.
        return

N = int(input())
N_lst = list(map(int, input().split()))
N_lst.sort()    # 우선 오름차순 정렬
M = int(input())
M_lst = list(map(int, input().split()))

for m in M_lst:
    # 검색(시작, 끝, 타겟)
    b_search(0,N-1,m)