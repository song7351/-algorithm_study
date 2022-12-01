"""
a,b 배열이 주어진다.
최대 k번 교환이 가능하다.
a의 최대합을 구하여라
"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

N, K = map(int, input().split())    # A의 최소값들을 B의 최대값과 비교해서 넣어줘야함
A = list(map(int, input().split())) # A는 오름차순정렬
B = list(map(int, input().split())) # B는 내림차순정렬

# 퀵정렬 - 오름차순
A2 = quick_sort(A)
# 라이브러리 - 내림차순
B.sort(reverse=True)

for i in range(K):
    if A2[i] < B[i]:
        A2[i], B[i] = B[i], A2[i]
    else:
        break

print(sum(A2))