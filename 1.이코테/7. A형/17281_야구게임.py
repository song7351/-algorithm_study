"""
1줄: N = 이닝
N줄: 9
"""
from itertools import permutations

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
player = list(set(permutations([1,2,3,4,5,6,7,8])))
max_score = 0

def g(now_idx, lst,game_score):
    global max_score
    for game in arr:
        out_stack = 0
        first_base, second_base, third_base = 0,0,0
        while out_stack < 3:        # 아웃스택이 3스택이상이면 해당 이닝종료
            if game[lst[now_idx]] == 0:
                out_stack += 1
            elif game[lst[now_idx]]  == 4:
                game_score += first_base + second_base + third_base + 1
                third_base, second_base, first_base = 0, 0, 0
            elif game[lst[now_idx]] == 3:
                game_score+= first_base + second_base + third_base
                third_base, second_base, first_base = 1, 0, 0
            elif game[lst[now_idx]] == 2:
                game_score += second_base + third_base
                third_base, second_base, first_base = first_base, 1, 0
            elif game[lst[now_idx]] == 1:
                game_score += third_base
                third_base, second_base, first_base = second_base, first_base, 1

            now_idx = (now_idx + 1) % 9

    if game_score > max_score:
        max_score = game_score
    return

#시작선수, 적용할순서,게임스코어
for p in player:
    g(5, list(p)+[0],0)

print(max_score)
