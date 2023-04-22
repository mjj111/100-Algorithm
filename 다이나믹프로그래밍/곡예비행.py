import sys

INT_MIN = -sys.maxsize
n, m = map(int, input().split())
graph = [[0 for j in range(m + 2)] for i in range(n + 2)]
dp = [[[INT_MIN for j in range(m+2)] for i in range(n+2)] for k in range(2)]

for i in range(0,n):
    graph[i][:m]=list(map(int,input().split()))


dp[0][n-1][0] = graph[n-1][0]
dp[1][n-1][m-1] =  graph[n-1][m-1]

for i in range(n-1, -1, -1):
    for j in range(0, m):
        if i == n-1 and j == 0: continue
        dp[0][i][j] = max(dp[0][i + 1][j], dp[0][i][j - 1]) + graph[i][j]

for i in range(n-1, -1, -1):
    for j in range(m-1, 0, -1):
        if i == n-1 and j == m-1: continue
        dp[1][i][j] = max(dp[1][i + 1][j], dp[1][i][j + 1]) + graph[i][j]

ans = INT_MIN
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[0][i][j] + dp[1][i][j])
print(ans)