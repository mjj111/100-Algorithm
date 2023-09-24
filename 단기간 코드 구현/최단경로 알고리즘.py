#다익스트라 알고리즘 

import heapq
import sys

input = sys.stdin.readline 
INF = sys.maxsize

n,m = map(int,input().split)
start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF] * n+1


for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # 큐에 본인을 0비용으로 넣는다. 
    distance[start] = 0 # 시작 노드 초기화
    
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: # 최단 거리 테이블의 값보다 dist가 크면 continue
            continue
    
        for i in graph[now]:
            cost = dist + i[1]  # cost : 현재 노드 now를 거쳐 다음 노드 i[1]로 가는 거리
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(start)




#벨만포드 알고리즘 
n , m = map(int, input().split()) # n 노드의 수 / m 간선의 수

graph = []

for i in range(m):
    u, v, w = list(map(int, input().split()))
    graph.append([u, v, w])


def BellmanFord(src):
    # 1. 최단거리 테이블 초기화 ( 출발노드 0 / 나머지 INF )
    dist = [float("inf") for i in range(n + 1)]
    dist[src] = 0

    # 2. 1~ n-1개의 노드를 사용한 최단거리 구하기 루프
    for i in range(n-1):
        for u, v, w in graph: # 입력받았던 그래프 돌기 /  u->v = w (비용)
            if dist[u] != float("inf") and dist[u] + w < dist[v]: 
            # 1) dist[u]가 INF가 아니고, 
            # 2) dist[u] + w (지금 계산한 최단거리) 가 dist[v] (기존 최단거리) 보다 작으면
                dist[v] = dist[u] + w # 테이블 갱신

    # 3. 음의 사이클 확인
    cycle = 0
    for u, v, w in graph:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            cycle = 1
            break
    if cycle == 0:
        print('Distance from source vertex',src)
        print('Vertex \t Distance from source')
        for i in range(1, len(dist)):
            print(i,'\t',dist[i])


BellmanFord(1)




#플로이드워셜 알고리즘 
INF = int(1e9)

# 노드 개수 & 간선 개수
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 경로 비용 = 0
for a in range(n+1):
    for b in range(n+1):
        if a==b:
            graph[a][b]=0

# 각 간선에 대한 정보 입력
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
# k -> a -> b 순서
for k in range(1, n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            # 점화식 그대로
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])