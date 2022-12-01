"""
시각
정수 N    (0 <= N <= 23)
00시 00분 00초 ~ N시 59분 59초까지 모든 시각 중에서 3이 하나라도 포함되는 모든 경우
"""
N = int(input())

cnt = 0
for h in range(N+1):        # 시
    for m in range(60):     # 분
        for s in range(60): # 초
            if '3' in str(h) or '3' in str(m) or '3' in str(s): # 문자열로 검사.
                cnt += 1

print(cnt)