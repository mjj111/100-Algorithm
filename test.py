import sys
from collections import deque

def topology_sort():
    result = []
    deq= deque()
    for i in range(n):
        if indegree[i] == 0 :
            deq.append(i)
    while deq:
        x = deq.popleft()
        result.append(x+1)
        for i in graph[x]:
            indegree[i] -=1
            if indegree[i] == 0:
                deq.append(i)
                
    if sum(indegree) >0: 
        print(0)   
    else:
        for i in result:
            print(i)
    

n, m = map(int, sys.stdin.readline().split()) 
indegree = [0] * n
graph = [[] for i in range(n)]

for _ in range(m):
    list_ = list(map(int, sys.stdin.readline().split()))
    for a, b in zip(list_[1:], list_[2:]):
        graph[a - 1].append(b - 1)  
        indegree[b - 1] += 1   

topology_sort()