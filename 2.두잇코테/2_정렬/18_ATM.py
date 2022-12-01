"""
https://www.acmicpc.net/problem/11399

삽입정렬.
- 선택한 인덱스의 값을 앞부분에 어디가 적절한 위치인지 탐색
- 찾으면 값을 선택한 인덱스까지 밀어주고 삽입한다.

sort= 68
선택정렬= 172
"""

n = int(input())
lst = list(map(int, input().split()))
# lst.sort()
for i in range(1,n):
    select_idx = i
    select_val = lst[i]
    for j in range(i-1,-1,-1):
        if lst[j] < select_val:
            select_idx = j+1
            break
    else:
        select_idx = 0

    for j in range(i,select_idx,-1):
        lst[j] = lst[j-1]
    lst[select_idx] = select_val

for i in range(1,n):
    lst[i] = lst[i]+lst[i-1]

print(sum(lst))