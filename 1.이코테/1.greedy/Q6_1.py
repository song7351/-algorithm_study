"""
https://school.programmers.co.kr/learn/courses/30/lessons/42891

먹어야할 음식 N개(1번~N번)
1초섭취 -> 다음음식 -> 반복
food_times: 각음식을 모두 먹는데 필요한 시간이 담겨있는 배열
K초: 네트워크가 장애가 발생한 시간
몇 번 음식부터 다시 섭취하면 되는지?
"""

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    N = len(food_times)
    food_idx = []
    for i in range(1, N+1):
        food_idx.append(i)

    while k > 0:
        food = food_times.pop(0) - 1
        idx = food_idx.pop(0)
        if food:
            food_times.append(food)
            food_idx.append(idx)
        k -= 1

    answer = food_idx[0]
    return answer

a = [4, 2, 3, 6, 7, 1, 5, 8]
b = 27

print(solution(a,b))
