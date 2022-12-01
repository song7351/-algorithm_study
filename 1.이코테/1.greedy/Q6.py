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

    answer = 0
    N = len(food_times)
    # K초 흐른다.
    for i in range(1,k+1):
        if food_times[answer]:
            food_times[answer] -= 1
            answer += 1
        else:
            while not food_times[answer]:
                answer += 1
                if answer == N:
                    answer = 0
            food_times[answer] -= 1
            answer += 1

        if answer == N:
            answer = 0

    # K초가 지난뒤 재시작 지점 idx = answer
    while not food_times[answer]:
        answer += 1
        if answer == N:
            answer = 0

    answer += 1
    if answer == N+1:
        answer = 1

    return answer


a = [3,1,2]
b = 5

print(solution(a,b))
