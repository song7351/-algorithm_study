"""
큰 수의 법칙
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 **가장 큰 수를 만드는 법칙**
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이법칙의 특징

"""
N, M, K = map(int, input().split())     # N:배열의크기, M:횟수, K:연속횟수
lst = list(map(int, input().split()))   # 예시: 2 4 5 4 6

first_max = 0
first_idx = 0

for i in range(N):                      # 첫번째 큰 수 출력
    if lst[i] > first_max:
        first_max = lst[i]
        first_idx = i

second_max = 0

for i in range(N):                      # 두번째 큰 수 출력
    if lst[i] > second_max and i != first_idx:
        second_max = lst[i]

ans = 0
first_cnt = 0
second_cnt = 1
while M > 0:
    if second_cnt == 1:                 # 첫번째 큰 수를 K번 연속
        ans += first_max
        first_cnt += 1
        M -= 1
        if first_cnt == K:
            second_cnt = 0
    if first_cnt == K:                  # 두번째 큰 수는 1번만 출력
        ans += second_max
        second_cnt += 1
        M -= 1
        if second_cnt == 1:
            first_cnt = 0

print(ans)