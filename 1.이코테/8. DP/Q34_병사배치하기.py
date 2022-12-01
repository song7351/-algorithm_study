"""
내림차순을 유지해야 한다.
남아있는 병수의 수가 최대로 되도록 하세요.
"""

n = int(input())
lst = list(map(int, input().split()))
memo = [1]*n

for i in range(1,n):
    for j in range(i):
        if lst[i] < lst[j]: # 만약 앞에서 현재값보다 큰게 있다면, 해당 길이에 +1한값이다. 그러나 기존에 입력된 길이값보다 작으면 무시한다.
            memo[i] = max(memo[i],memo[j]+1)
print(memo)
print(n - max(memo))