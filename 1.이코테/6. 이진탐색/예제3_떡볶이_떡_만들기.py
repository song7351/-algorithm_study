"""
1줄: N M 떡의개수, 요청떡의길이
2줄: Ni ~
목표 떡의 길이를 챙기는 가장 높은 H의 값은?
M = (H-Ni) + (H-Nii) + ....
"""
def b_search(start, end, target):
    global ans
    if start <= end:
        middle = (start+end)//2
        tmp = 0             # middle로 떡의 길이를 잘랐을때 손님이 가져가는 떡의 길이
        for tteog in lst:
            if tteog < middle:  # 떡의 길이가 middle보다 작다면, 제외
                continue
            else:
                tmp += (tteog - middle)
        if tmp >= target:       # tmp를 구했는데 목표치보다 크거나 작을때
            if middle > ans:    # 높이(middle)의 최대값을 구해라.
                ans = middle

        if tmp <= target:       # 만약 손님이 가져갈 떡이 목표치보다 적다면, 너무 높게 middle을 잡았다.
            b_search(start, middle-1, target)
        else:                   # 만약 손님이 가져갈 떡이 목표치보다 많다면, 너무 낮게 middle을 잡았다.
            b_search(middle+1, end, target)

N, M = map(int,input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = 0
b_search(1,lst[-1],M)
print(ans)