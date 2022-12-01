n = int(input())
memo = [0]*(n+1)
a_lst = []
b_lst = []
ans = 0
for i in range(n):
    a,b = map(int,input().split())
    a_lst.append(a)
    b_lst.append(b)

for i in range(n-1, -1, -1):
    d = i+a_lst[i]                              # 연순으로 날짜를 검사하는데
    if d <= n:                                  # 만약 오늘날(i)를 실행할시 기간(n)을 초과하면, 실행할
        memo[i] = max(memo[d]+b_lst[i], ans)
        ans = memo[i]
    else:                                       # 만약 오늘날(i)를 실행할시 기간(n)을 초과하면, 실행할 수 없으므로 현재 최대값을 설정한다.
        memo[i] = ans

print(ans)