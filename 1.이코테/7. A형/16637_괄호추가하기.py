N = int(input())
lst = list(input())
used = [0]*N
ans = -(2**31)                          # 문제에서 제시한 최소값

def yeonsan(arr, result):
    global ans
    for i in range(1,len(arr)-1):
        if arr[i] == '+':
            result += int(arr[i+1])
        elif arr[i] == '-':
            result -= int(arr[i+1])
        elif arr[i] == '*':
            result *= int(arr[i+1])

    if result > ans:
        ans = result

def gwalho(arr,check):
    tmp = 0
    k = check+2                     # 연달아서 괄호를 설정할 수 없기 때문에 +2
    if check == 0:
        k = 1
    for i in range(k,len(arr)):
        if not arr[i].isdigit():                            # 괄호부분 설정
            if arr[i] == '+':
                tmp = int(arr[i-1]) + int(arr[i+1])
            elif arr[i] == '-':
                tmp = int(arr[i-1]) - int(arr[i+1])
            elif arr[i] == '*':
                tmp = int(arr[i-1]) * int(arr[i+1])
            new_arr = arr[:i-1] + [str(tmp)] + arr[i+2:]    # 괄호부분 계산후 새로운 리스트
            yeonsan(new_arr, int(new_arr[0]))               # 연산 연산보기
            if len(new_arr) > 3:                            # break 조건 예)a+b만 남을경우 괄호치기 중지
                gwalho(new_arr,i)                           # 괄호처리한 부분의 인덱스를 넘긴다.
if N > 1:
    yeonsan(lst, int(lst[0]))   # 초기 정답 설정.
    gwalho(lst,0)
if N == 1:
    ans = int(lst[0])
print(ans)

