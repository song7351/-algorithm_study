"""
https://www.acmicpc.net/problem/2751
오름차순으로 정렬하기
sort - 1708
count - 960
merge - 7768

병합정렬
1. 2개의 그룹으로 쪼갠다.a
2. 더이상 쪼갤 수 없을때 순서를 정리한다.
3. 2개의 그룹을 합친다.
"""
import sys
input = sys.stdin.readline

def merge_sort(s,e):
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
A = [0] * int(n+1)
tmp = [0] * int(n+1)
for i in range(1, n+1):
    A[i] = int(input())

merge_sort(1,n)

for i in range(1,n+1):
    print(A[i])