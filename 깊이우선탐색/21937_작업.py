import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n,m = map(int,input().split())
connections = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    connections[b].append(a)
wanna_do_node = int(input())

cnt = 0
def how_many_work_to_do(node):
    global cnt 
    visited[node] = 1 
    for i in connections[node]:
        if not visited[i]:
            cnt +=1 
            how_many_work_to_do(i)
            
how_many_work_to_do(wanna_do_node)
print(cnt)