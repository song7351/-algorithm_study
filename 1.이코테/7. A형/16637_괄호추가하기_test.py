N = int(input())
lst = list(input())
used = [0]*N
ans = int(lst[0])

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

def gwalho(arr):
    tmp = 0
    for i in range(len(arr)):
        if not arr[i].isdigit():
            if arr[i] == '+':
                tmp = int(arr[i-1]) + int(arr[i+1])
            elif arr[i] == '-':
                tmp = int(arr[i-1]) - int(arr[i+1])
            elif arr[i] == '*':
                tmp = int(arr[i-1]) * int(arr[i+1])
            new_arr = arr[:i-1] + [str(tmp)] + arr[i+2:]
            yeonsan(new_arr, int(new_arr[0]))
            if len(new_arr) > 3:
                gwalho(new_arr)
if N > 1:
    yeonsan(lst, ans)   # 초기 정답 설정.
    gwalho(lst)

print(ans)

