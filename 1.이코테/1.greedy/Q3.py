"""
문자열 S는 0과 1로만으로 구성
다솜이는 S문자열을 모두 같도록 설정한다.
뒤집기 (0->1 , 1->0)으로 뒤집는 최소 횟수는?
단, 연속된 숫자는 한번에 뒤집을 수 있다.
ex) 0001100 -> 1회: 0000000

연속된 그룹(0혹은 1)중 가장 적은 그룹의 개수를 구한다.
ex) 0001100 -> 0은 2개, 1은 1개, 정답 1
"""

S = list(map(int,input()))
zero_cnt = 0
one_cnt = 0

if S[0] == 0:               # 첫번째 인덱스에 따른 cnt 설정
    zero_cnt += 1
else:
    one_cnt += 1

for i in range(1, len(S)):  # 인덱스의 이전것과 다를 경우, 각각 cnt +1
    if S[i] != S[i-1]:
        if S[i] == 0:
            zero_cnt += 1
        else:
            one_cnt += 1

print(min([zero_cnt, one_cnt]))
