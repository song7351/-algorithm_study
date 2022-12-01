"""
소인수만을 약수로 가지는 합성 수
n번째 못생긴 수는?
무지성으로 나눠서 확인한다.
"""
n = int(input())
lst = [1,2,3,4,5]
num = 5
while len(lst) < n:
    num += 1
    tmp = num
    for i in range(10):
        cnt = 0
        if tmp%2 == 0:
            tmp = tmp//2
        else:
            cnt += 1

        if tmp%3 == 0:
            tmp = tmp//3
        else:
            cnt += 1

        if tmp%5 == 0:
            tmp = tmp//5
        else:
            cnt += 1

        if tmp == 1:
            break
        if cnt == 3:
            break
    if tmp == 1:
        lst.append(num)

print(lst[n-1])