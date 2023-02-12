import sys
input = sys.stdin.readline

#플로이드 와샬 알고리즘이란?  
#양 또는 음의 에지 가중치를 갖는 방향 가중 그래프에서 각각의 정점에서 정점까지의
#모든 최단 경로를 찾는 알고리즘이다.
N = int(input().rstrip())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]

for k in range(0, N):   # 경유지를 위해 
    for i in range(0, N):   
        for j in range(0, N):
            if matrix[i][k]==1 and matrix[k][j]==1:
                matrix[i][j] = 1


for m in matrix:
    print(*m)