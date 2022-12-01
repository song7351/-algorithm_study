tc = int(input())

for _ in range(tc):
    N = int(input())
    lst = list(map(int, input().split()))
    mine = list(map(str, input().split()))

    for i in range(N):
        if i == 0:
