n = int(input())
memo = [0]*30

for i in range(n):
    a,b = map(int,input().split())
    if memo[i] == 0 and i != 0:
        memo[i] = max(memo[:i])
    memo[i+a] = max(memo[i+a], memo[i]+b)

# print(memo)
print(max(memo[:n+1]))