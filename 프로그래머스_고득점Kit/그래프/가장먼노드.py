from collections import deque
def solution(n, vertex):
    visited = [0] * (n+1)
    visited[1] = -1
    edges = [[] for _ in range(n+1)]
    for i in vertex:
        edges[i[0]].append(i[1])
        edges[i[1]].append(i[0])
    q = deque()
    q.append([1,0])
    while q:
        now_node,now_depth = q.popleft()
        for next_node in edges[now_node]:
            if visited[next_node] == 0:
                visited[next_node] = now_depth + 1 
                q.append([next_node, now_depth + 1] )
    answer = 0 
    for i in visited:
        if i == max(visited):
            answer += 1
    return answer