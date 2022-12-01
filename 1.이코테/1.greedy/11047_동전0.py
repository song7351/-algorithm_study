"""
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
"""

N, K = map(int, input().split())

lst = []
for _ in range(N):
    lst.append(int(input()))

cnt = 0

for i in range(N-1, -1, -1):
    if K // lst[i] != 0:
        cnt += K//lst[i]
        K = K % lst[i]

print(cnt)