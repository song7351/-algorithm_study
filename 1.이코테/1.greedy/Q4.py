"""
편의점 주인 동빈이는 N개의 동전을 가지고있다.
N개의 동전을 이용하여 **만들 수 없는** 양의 정수 금액 중 최솟값은?
1줄: N
2줄: n1 n2 n3 ... N개. ni원
"""

N = int(input())
lst = list(map(int, input().split()))
check = [[]]                            # 부분집합 집합
ans = []                                # 부분집합의 합
for i in lst:
    n = len(check)
    for j in range(n):
        check.append(check[j] + [i])
        ans.append(sum(check[j]) + i)

num = 1
result = 0
while True:                             # 1부터 검색해서 부분집합의 합 리스트에 없다면 결과.
    if num not in ans:
        result = num
        break
    else:
        num += 1
print(result)


