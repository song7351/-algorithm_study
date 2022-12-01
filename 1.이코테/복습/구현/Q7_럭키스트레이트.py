"""
정답: 왼쪽 절반, 오른쪽절반의 합이 같아야 한다.
"""

n = list(input())
n = [ int(i) for i in n ]
ans = "READY"
a = sum(n[:len(n)//2])
b = sum(n[len(n)//2:])
if a == b:
    ans = "LUCKY"
print(ans)