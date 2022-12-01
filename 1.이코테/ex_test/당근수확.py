test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    lst = list(map(int, input().split()))
    min_diff = int(1e9)
    ans = 0
    sum_lst = sum(lst)
    carrot = 0
    for i in range(N):
        carrot += lst[i]
        if abs(sum_lst - carrot - carrot) < min_diff:
            ans = i+1
            min_diff = abs(sum_lst - carrot - carrot)

    print(f"#{tc} {ans} {min_diff}")