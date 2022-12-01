"""
성적이 낮은순서대로 학생이름을 출력해주세요.
"""

N = int(input())
name_lst = []
score_lst = []
for i in range(N):
    name,score = input().split()
    name_lst.append(name)
    score_lst.append(int(score))

# 삽입정렬
for i in range(1,len(score_lst)):
    for j in range(i, 0, -1):
        if score_lst[j] < score_lst[j-1]:
            score_lst[j], score_lst[j-1] = score_lst[j-1], score_lst[j]
            name_lst[j],  name_lst[j-1] = name_lst[j-1], name_lst[j]
        else:
            break

print(*name_lst)