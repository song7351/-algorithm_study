"""
문자열 재정렬
알파벳 대문자와 숫자(0~9)로만 구성된 문자열을 입력
모든 알파벳을 오름차순으로 정렬하여 먼저 문자열을 재구성한뒤 모든 숫자를 더한 값을 붙여서 출력해라

"""

N = list(input())
num = 0
word = []

for i in N:
    if i.isdigit():         # 숫자판별
        num += int(i)
    else:
        word.append(i)
word.sort()                 # 오름차순
ans = ''.join(word) + str(num)

print(ans)