"""
https://school.programmers.co.kr/learn/courses/30/lessons/60061
2차원 벽면은 n x n 크기 정사각 격자 형태
n은 5 이상 100 이하인 자연수
build_frame의 원소는 [x, y, a, b]형태
x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
a는  0은 기둥, 1은 보를 나타냅니다.
b는  0은 삭제, 1은 설치를 나타냅니다.
벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.
바닥에 보를 설치 하는 경우는 없습니다.,
보는 항상 오른쪽 방향으로 설치됩니다.

return 하는 배열의 원소는 [x, y, a] 형식
xya 순서로 오름차순 정렬
x, y는 기둥, 보의 교차점 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
a  0은 기둥, 1은 보를 나타냅니다.
"""
def build(x,y,a,result):
    if a:   # 만약에 보라면
        # 보위치 아래 혹은 오른쪽 아래에 기둥이 있는가?
        for test in [[x,y-1,0],[x+1,y-1,0]]:
            if test in result:
                result.append([x,y,a])
                return result
        # 보위치의 왼쪽 오른쪽에 보가 있는가?
        if [x-1,y,1] in result and [x+1,y,1] in result:
            result.append([x,y,a])
            return result
    else:   # 만약에 기둥이라면
        # 기둥이 바닥으로부터 설치를 하는가?
        if y == 0:
            result.append([x,y,a])
            return result
        # 기둥의 아래가 기둥이거나 현재자리 혹은 왼쪽이 보인가?
        for test in [[x,y-1,0],[x,y,1], [x-1,y,1]]:
            if test in result:
                result.append([x,y,a])
                return result
    # 만약 모든조건이 해당하지 않는다면 추가하지말고 그냥 다시 돌려주세요.
    return result

def destroy(x,y,a,result):
    # 일단 삭제요청이 들어오면 삭제하세요.
    result.remove([x, y, a])
    ans = [item[:] for item in result]
    for items in result:
        test = build(items[0],items[1],items[2],ans)
        if len(test) == len(result):
            result.append([x,y,a])
            return result
        else:
            ans.remove([items[0],items[1],items[2]])
    else:
        return result

def solution(n, build_frame):
    result = []
    for item in build_frame:
        x,y,a,b = item[0], item[1], item[2], item[3]
        if b == 1:
            result = build(x,y,a,result)
        else:
            result = destroy(x,y,a,result)
        #print(result)
    result.sort(key=lambda z:(z[0],z[1],z[2]))
    #print(result)
    return result

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
#[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

#build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
#[[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]
print(solution(n,build_frame))