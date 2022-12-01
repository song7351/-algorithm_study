"""
거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다.
손님에게 거슬러 줘야 할 돈이 N원이 일때, 거슬러 줘야 할 동전의 **최소 개수**를 구하여라
단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
"""

N = int(input())    # 손님에게 거슬러 줘야 할 금액
cnt = 0             # 거슬러 줘야 할 돈전의 개수

jandon = [500, 100, 50, 10]

for i in jandon:
    cnt += N // i
    N = N % i

print(cnt)