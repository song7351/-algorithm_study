"""
숫자 카드 게임
숫자가 놓은 카드들이 N * M 형태로 놓여있다. (행 * 열)
먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
선택된 행에 포함된 카드들 중 **가장 숫자가 낮은 카드**를 뽑아야한다.
그러므로 각 행의 가장 숫자가 낮은 카드들중 가장 큰 카드를 뽑아야 한다.

"""
N, M = map(int, input().split())    # 행, 열의 개수
board = [list(map(int, input().split())) for _ in range(N)]     # 게임판

min_card = [0] * N          # 각 행의 최소값
for i in range(N):          # 각 행을 선택
    min_num = 10000         # 카드는 1~10000의 값을 가진다.
    for j in range(M):      # 선택된 행의 열을 검색
        if board[i][j] < min_num:
            min_num = board[i][j]
    min_card[i] = min_num

ans = 0                     # 각행의 최소값 모음중 큰값을 찾는다.
for i in range(N):
    if min_card[i] > ans:
        ans = min_card[i]

print(ans)
