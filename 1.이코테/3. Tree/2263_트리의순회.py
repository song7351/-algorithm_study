"""
n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다.
이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때,
프리오더를 구하는 프로그램을 작성하시오.
"""
N = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

lst = [0] * (N+1)
