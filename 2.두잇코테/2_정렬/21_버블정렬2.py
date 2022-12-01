"""
버블정렬이 몇번 발생하는가?
8
3 2 8 1 7 4 5 6

https://www.acmicpc.net/problem/1517
병합정렬로 푸는 문제
- 버블소트 n^2
- 병합정렬 nlogn
- 기본적으로 병합정렬도 인접 값과 swap이 발생하고 이는 bubble소트와 동일한것처럼 보임
- 그러나 합쳐지고 다시 정렬할때는 버블 정렬이 아님. 그럼 어떻게 버블정렬 카운트를 하는가?
- 간단하게 왼쪽 / 오른쪽 리스트가 있다고 봤을때,
- 왼쪽리스트는 고정되어있다고 생각하고 오른쪽 리스트의 첫번째가 왼쪽 보다 작다면,
- 해당 왼쪽 리스트를 전부 버블 소트로 제꼈다고 봐도 무방하다.
- 수정렬하기2와 코드가 동일하나 한줄 정도가 다르다.

"""
import sys
input = sys.stdin.readline

def merge_sort(s,e):
    global cnt
    if e-s < 1:
        return

    m = int(s + (e-s) / 2)
    merge_sort(s,m)
    merge_sort(m+1, e)
    for i in range(s, e+1):
        tmp[i] = A[i]

    k = s
    index1 = s
    index2 = m + 1

    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
            # 특이점!
            cnt += m - index1 + 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1


    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

n = int(input())
A = [0] + list(map(int, input().split()))
tmp = [0] * int(n+1)

cnt = 0
merge_sort(1,n)
print(cnt)