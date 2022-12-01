"""
https://school.programmers.co.kr/learn/courses/30/lessons/60057
"aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현
s의 길이는 1 이상 1,000 이하입니다.
"""

def solution(s):
    word = list(s)
    N = len(word)
    n = len(word)//2    # 길이는 최대 절반까지만 의미가 있다.
    answer = len(word)
    for i in range(1,n+1):  # 단어를 얼만큼 자를것인가?
        cnt = 1
        for j in range(N-i):
            idx = j
            min_len = len(word)
            while True:
                if idx >= N-1 or idx + i >N-1:
                    break
                if word[idx:idx+i] == word[idx+i:idx+i+i]:
                   cnt += 1
                   if idx+i+i == N:
                       min_len = min_len - (cnt - 1) * i
                       if cnt < 10:
                           min_len += 1
                       elif cnt < 100:
                           min_len += 2
                       elif cnt < 1000:
                           min_len += 3
                       else:
                           min_len += 4
                       cnt = 1
                else:
                    min_len = min_len - (cnt - 1) * i
                    if cnt == 1:
                        pass
                    elif cnt<10:
                        min_len += 1
                    elif cnt < 100:
                        min_len += 2
                    elif cnt < 1000:
                        min_len += 3
                    else:
                        min_len += 4
                    cnt = 1
                idx = idx + i
            if min_len < answer:
                answer = min_len
    return answer

a = "xababcdcdababcdcd"
print(solution(a))