arr1 = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
arr2 = ["fro??", "????o", "fr???", "fro???", "pro?"]
def search(s,e,q,w):
    if s <= e:
        m = (s+e)//2
        if q[m] != '?' and q[m] != w[m]:
            return False
        elif q[m] == '?' or q[m] == w[m]:
            if search(s,m-1,q,w):
                if search(m+1,e,q,w):
                    return True
                else:
                    return False
            else:
                return False
    else:
        return True

def solution(words, queries):
    answer = []
    for q in queries:
        nq = len(q)
        cnt = 0
        for w in words:
            nw = len(w)
            if nq == nw:
                if search(0,nw-1,q,w):
                    cnt += 1
        answer.append(cnt)
    return answer

print(solution(arr1,arr2))