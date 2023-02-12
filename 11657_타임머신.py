import sys
input = sys.stdin.readline
INF = int(1e9)

#벨만 포드 알고리즘 가중치(비용)이 음수가 가능하다. 
n, m = map(int, input().split())
edges = []
dist = [INF]*(n+1)

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u,v,w))

def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if dist[node]!=INF and dist[next_node]>cost+dist[node]:
                dist[next_node] = dist[node]+cost
                if i == n-1: 
                    return True
    return False

n_c = bf(1)

if n_c:
    print("-1")
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])