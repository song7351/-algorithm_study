test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    stop_lst = [0]*5001
    for _ in range(N):
        x,y = map(int, input().split())
        for i in range(x,y+1):
            stop_lst[i] += 1
    P = int(input())
    print(f"#{tc}", end=" ")
    for _ in range(P):
        print(stop_lst[int(input())], end=" ")
    print()