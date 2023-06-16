import heapq

def dijkstra(start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue) #최대 힙  
        dist = -1 * dist # - 로 저장해놨었기 때문 

        if now == end:
            print(dist)
            break

        if distance[now] > dist: # 이미 최대 중량인경우
            continue

        for i in graph[now]: 
            if dist == 0:# 처음이라면 
                distance[i[1]] = i[0] # 거리 갱신 
                heapq.heappush(queue, (-distance[i[1]], i[1]))
                
                
            # 기존에 저장된 값이 dist(이전 도시에서의 최대중량)와 현재 다리 최대 중량 보다 작다면!(중복 연결)
            elif distance[i[1]] < i[0]  and distance[i[1]] < dist: 
                distance[i[1]] = min(dist, i[0])
                heapq.heappush(queue, (-distance[i[1]], i[1]))



n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

distance = [0] * (n + 1)
start, end = map(int, input().split())

dijkstra(start, end)