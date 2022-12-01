"""
원리
1. 첫번째 인덱스부터 전체중에 가장 작은수랑 교환한다.
2. 두번째 인덱스부터 전체중에 가장 작은수랑 교환한다.
3. .....

"""
arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]