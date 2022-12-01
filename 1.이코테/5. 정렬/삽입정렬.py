"""
원리
1. 삽입정렬은 두 번째 데이터부터 시작한다. why? 첫 번째 데이터는 그 자체로 정렬되어있다고 판단.
2. 두번째 인덱스부터 확인하는데....
3.  검사를 시작하는 인덱스부터 이전인덱스 방향으로 검사를 진행.
    3-1. 진행중 작다면, 교환해주고 아니라면 break
"""
arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(arr)):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1],arr[j]
        else:
            break

print(arr)