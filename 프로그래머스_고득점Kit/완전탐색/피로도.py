answer = 0

def dfs(n,visited,k, cnt, dungeons):
    global answer 
    if cnt > answer:
        answer = cnt

    for j in range(n):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(n,visited,k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global answer 
    n = len(dungeons)
    visited = [0] * n
    dfs(n,visited,k, 0, dungeons)
    return answer