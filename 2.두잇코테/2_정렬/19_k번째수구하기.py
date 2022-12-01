"""
https://www.acmicpc.net/problem/11004

k(k-1)번째 수를 구해라
sort = 4200
방법(1) 시간초과
방법(2) 시간초과

"""
import sys
sys.setrecursionlimit(10**6)

# 방법1
# def quick_sort(arr):
#     if len(arr) < 2:
#         return arr
#
#     pivot = arr[0]
#     tail = arr[1:]
#     left_lst = [x for x in tail if x <= pivot]
#     right_lst = [x for x in tail if x > pivot]
#
#     return quick_sort(left_lst) + [pivot] + quick_sort(right_lst)

# 방법2
# def quick_sort(arr):
#     if len(arr) < 2:
#         return arr
#
#     pivot = len(arr)-1
#     start = 0
#     end = len(arr)-2
#
#     while start < end:
#         if arr[start] <= arr[pivot]:
#             start += 1
#         if arr[end] > arr[pivot]:
#             end -= 1
#         if arr[end] < arr[pivot] < arr[start]:
#             arr[end], arr[start] = arr[start], arr[end]
#             start += 1
#             end -= 1
#
#     if arr[start] > arr[pivot]:
#         return quick_sort(arr[:start]) + [arr[pivot]] + quick_sort(arr[start:pivot])
#     else:
#         return quick_sort(arr[:start+1]) + [arr[pivot]] + quick_sort(arr[start+1:pivot])


input = sys.stdin.readline

n,k = map(int, input().split())
k -= 1
lst = list(map(int, input().split()))

# lst.sort()
# 퀵정렬(1)
# new_lst = quick_sort(lst)
# print(new_lst[k])

