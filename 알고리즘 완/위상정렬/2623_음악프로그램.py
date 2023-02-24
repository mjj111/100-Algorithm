import sys
from collections import deque
#위상정렬
def topology_sort():
    result = []
    q = deque()
    for i in range(n):
        if indegree[i] == 0: 
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now + 1) 
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:  
                q.append(i)

    if sum(indegree) > 0: 
        print(0)
    else:
        [print(i) for i in result]

n, m = map(int, sys.stdin.readline().split()) 
indegree = [0] * n
graph = [[] for i in range(n)]

for _ in range(m):
    list_ = list(map(int, sys.stdin.readline().split()))
    for a, b in zip(list_[1:], list_[2:]):
        graph[a - 1].append(b - 1)  
        indegree[b - 1] += 1   

topology_sort()