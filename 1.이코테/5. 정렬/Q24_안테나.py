"""
안테나를 한집에 설치했을때 각집과 안테나의 거리의 합이 최소를 출력하세요.
괜히 선택정렬써봤는데 시간초과나니깐 sort쓰십쇼....
"""

N = int(input())
house = list(map(int,input().split()))
house.sort()
print(house[(N-1)//2])
