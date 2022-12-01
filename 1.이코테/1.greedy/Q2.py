"""
문자열 S는 각자리가 숫자(0~9)로 구성.
왼쪽부터 오른쪽으로 * 혹은 + 연산자를 넣어 가장 큰 수를 만드세요.
"""

S = list(map(int, input()))

ans = 0

for i in range(len(S)):
    if i == 0:                      # 첫번째 수 설정
        ans += S[i]
    elif ans + S[i] > ans * S[i]:   # 더하기 혹은 곱하기중 큰거를 정한다.
        ans = ans + S[i]
    else:
        ans = ans * S[i]

print(ans)