"""
자물쇠크기 N * N
열쇠크기 M * M
"""
# 시계방향으로 회전
def rotate(k):
    n = len(k)
    KEY = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            KEY[j][n-i-1] = k[i][j]
    return KEY

def check(key,board,lock):
    m = len(key)
    n = len(lock)
    # board초기화를 위해서 새로운 board를 만든다.
    test = [item[:] for item in board]
    x,y = 0,0
    # 열쇠크기를 고려해서 시작점 설정
    for i in range(3*n-m):
        for j in range(3*n-m):
            cnt = 0
            x = 0
            # 열쇠삽입
            for k in range(i,i+m):
                y = 0
                for l in range(j,j+m):
                    test[k][l] += key[x][y]
                    y += 1
                x += 1
            
            # 열쇠삽입후 실제자물쇠(보드판의가운데)가 전부 1인가?
            for k in range(n,2*n):
                for l in range(n,2*n):
                    if test[k][l] == 1:
                        cnt += 1
            
            # 전부 1이면 return true
            if cnt == n*n:
                return True
            else:
            # 자물쇠가 틀리면, board초기화
                test = [item[:] for item in board]
    return False

def solution(key, lock):
    N = len(lock)
    # 자물쇠판크기 3배로 확장.
    board = [[0]*(3*N) for _ in range(3*N)]
    answer = False
    x,y = 0,0
    # 확장판의 한가운데 기존 자물쇠 삽입
    for i in range(N, 2*N):
        y = 0
        for j in range(N, 2*N):
            board[i][j] = lock[x][y]
            y += 1
        x += 1
    # 회전은 총 4번
    for _ in range(4):
        # 키회전
        key = rotate(key)
        # 회전한키 확인
        answer = check(key, board, lock)
        if answer:
            return answer
    return answer


# True
a = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
b = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(a,b))