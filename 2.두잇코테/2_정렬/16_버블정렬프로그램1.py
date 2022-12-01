"""
https://www.acmicpc.net/problem/1377

문제목표: 버블소트가 한번도 일어나지않는 순번을 구해라.
1차시도: 걍 버블소트해서 직접 뽑는것 = 시간초과(n^2)
answer
- 버블소트는 n^2복잡도 때문에 시간초과 발생
- 그러니 좀 더 빠른 sort로 정렬(nlogn)
- 근데 그러면 몇번 정렬에 끝나는지 알 수 없음
- 그래서 저장할때 인덱스값도 같이 저장해준다.
- 이동후 인덱스값과 기존 인덱스값의 차이중 큰값 + 1을 해준다.
- 왜냐? 해당 차이 값의 뜻은 양수일때 왼쪽으로 밀려간 거리를 뜻하는데
- 항상 오른쪽 끝부터 값이 차기 때문에 가장 많이 왼쪽으로 밀려난값이 버블정렬을 끝난 때이다.
- 근데 우리는 버블소트가 한번도 일어나지 않는 순번을 구해야되므로 +1을 해준다.
"""
import sys
input = sys.stdin.readline

n = int(input())
lst = [(int(input()), i) for i in range(n)]
lst.sort()

maxV = 0
for i in range(n):
    if maxV < lst[i][1] - i:
        maxV = lst[i][1] - i

print(maxV + 1)



