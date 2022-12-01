"""
<수정>
https://www.acmicpc.net/problem/1427
내림차순 정렬
선택정렬 - 가장 앞부터 채우는 정렬
"""
n = list(input())
n_lst = list(map(int, n))
# n_lst.sort(reverse=True)
m = len(n_lst)
for i in range(m):
    maxV = i
    for j in range(m-1, i, -1):
        if n_lst[j] > n_lst[maxV]:
            maxV = j

    n_lst[i], n_lst[maxV] = n_lst[maxV], n_lst[i]

n_lst = list(map(str, n_lst))
print(''.join(n_lst))
