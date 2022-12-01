"""
1줄: N = 이닝
N줄: 9
"""
def f(i,n):
    if i == n:
        new_player = player[:3] + [0] + player[3:]
        grp.append(new_player)
    else:
        for j in range(i,n):
            player[i], player[j] = player[j], player[i]
            f(i+1,n)
            player[i], player[j] = player[j], player[i]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
player = [1,2,3,4,5,6,7,8]
grp = []
max_score = 0
f(0,8)

def g(innings, end, now_idx, lst,game_score):
    global max_score
    if innings > end:
        if game_score > max_score:
            max_score = game_score
        return
    out_stack = 0
    base = [0,0,0,0]
    while out_stack < 3:        # 아웃스택이 3스택이상이면 해당 이닝종료
        if arr[innings][lst[now_idx]] == 0:
            out_stack += 1
        else:
            if arr[innings][lst[now_idx]]  == 4:
                game_score += 1
            for j in range(3,0,-1):
                if base[j] != 0:
                    base[j] += arr[innings][lst[now_idx]]
                if base[j] > 3:
                    game_score += 1
                    base[j] = 0
                else:
                    base[base[j]] = base[j]
                    base[j] = 0
                if j == arr[innings][lst[now_idx]] :
                    base[j] = arr[innings][lst[now_idx]]

        now_idx = (now_idx + 1) % 10
    g(innings+1, end, now_idx,lst,game_score)

#0번째 게임부터, N-1번째 게임, 시작선수, 적용할순서,게임스코어
for i in range(len(grp)):
    g(0,N-1,0, grp[i],0)

print(max_score)
