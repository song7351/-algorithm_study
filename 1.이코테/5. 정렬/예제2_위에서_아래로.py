"""
내림차순으로 출력하시오
"""

N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))

for i in range(N):
    max_index = i
    for j in range(i+1, N):
        if lst[max_index] < lst[j]:
            max_index = j
    lst[i], lst[max_index] = lst[max_index], lst[i]

print(*lst)