arr1 = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
arr2 = ["fro??", "????o", "fr???", "fro???", "pro?"]
def solution(words, queries):
    answer = []
    for q in queries:
        nq = len(q)
        cnt = 0
        for w in words:
            nw = len(w)
            if nq == nw:
                for i in range(nw):
                    if q[i] == '?':
                        continue
                    elif q[i] != w[i]:
                        break
                else:
                    cnt += 1
        answer.append(cnt)

    return answer

print(solution(arr1,arr2))