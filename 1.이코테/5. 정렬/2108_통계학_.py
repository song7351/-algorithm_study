N = int(input())

lst = list(int(input()) for _ in range(N))
lst.sort()

print(round(sum(lst)/N))
print(lst[N//2])

dict_N = dict()

start = lst[0]
maxC = 0
cnt = 1
maxV = []
for i in range(1, N):
    if start == lst[i]:
        cnt += 1
        if i == N-1:
            if cnt > maxC:
                maxC = cnt
                maxV = [lst[i - 1]]
            elif cnt == maxC:
                maxV.append(lst[i - 1])
    else:
        if cnt > maxC:
            maxC = cnt
            maxV = [lst[i-1]]
        elif cnt == maxC:
            maxV.append(lst[i-1])
        cnt = 1
        start = lst[i]

if N == 1:
    print(lst[0])
else:
    if len(maxV) == 1:
        print(maxV[0])
    else:
        print(maxV[1])
print(lst[-1] - lst[0])