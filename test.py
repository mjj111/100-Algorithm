import sys

INF_MIN = -sys.maxsize
n, m = map(int, input().split())
graph = [[0 for j in range(m + 2)] for i in range(n + 2)]
dp = [[[INF_MIN for j in range(m + 2)] for i in range(n + 2)] for k in range(2)]

for i in range(1, n + 1): 
    graph[i][1:m+1]=list(map(int,input().split()))

dp[0][n][1], dp[1][n][m] = graph[n][1], graph[n][m]

#상승 
for i in range(n, 0, -1):
    for j in range(1, m + 1, 1):
        if i == n and j == 1: continue  #밑과 왼쪽을 비교해서 출발한 비행  중 가장 점수가 높은 것과 현재 점수를 합하여 지금까지 상승방향으로 도달한 위치에서 얻을 수 있는 가장 높은 점수다. 
        dp[0][i][j] = max(dp[0][i + 1][j], dp[0][i][j - 1]) + graph[i][j]
#하강 
for i in range(n, 0, -1):
    for j in range(m, 0, -1):
        if i == n and j == m: continue  # 밑과 오른쪽을 비교해서 골인한 비행 중 가장 점수가 높은 것과 현재 점수를 합하여 마지막 점수에서 지금까지 하강 방향으로 도달한 위치에서 얻을 수 있는 가장 높은 점수다. 
        dp[1][i][j] = max(dp[1][i + 1][j], dp[1][i][j + 1]) + graph[i][j]

ans = INF_MIN
for i in range(1, n + 1):
    for j in range(1, m + 1):
        ans = max(ans, dp[0][i][j] + dp[1][i][j])
print(ans)