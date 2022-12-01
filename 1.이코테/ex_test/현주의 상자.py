test_case = int(input())

for tc in range(1, test_case+1):
    N, Q = map(int,input().split())
    box_lst = [0]*N
    for i in range(1, Q+1):
        L, R = map(int,input().split())
        for j in range(L-1, R):
            box_lst[j] = i
    print(f"#{tc}", end=" ")
    for i in range(N):
        print(box_lst[i], end=" ")
    print()