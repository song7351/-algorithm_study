"""
최초 1이 못생긴 수일때
*2, *3, *5는 못생긴 수의 배수이므로 못생긴 수이다. == 1로 표기

"""
n = int(input())

memo = [0]*n
memo[0] = 1
i2,i3,i5 = 0,0,0
v2,v3,v5 = 2,3,5

for i in range(1,n):
    memo[i] = min(v2,v3,v5)
    if memo[i] == v2:
        i2 += 1
        v2 = memo[i2]*2
    if memo[i] == v3:
        i3 += 1
        v3 = memo[i3]*3
    if memo[i] == v5:
        i5 += 1
        v5 = memo[i5]*5

print(memo[n-1])