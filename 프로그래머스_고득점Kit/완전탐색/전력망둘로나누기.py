# from collections import deque 
# def bfs(start,visited,graph):
#     result = 0
#     que = deque()
#     que.append(start)
#     while(que):
#         now = que.popleft()
#         visited[now] = True 
#         for next in graph[now]:
#             if visited[next] ==False :
#                 que.append(next)
#                 result +=1 
    

# def solution(n, wires):
#     graph = [[] for _ in range(n+1)]
#     print(graph)
#     answer = 101
#     for v1,v2 in wires:
#         graph[v1].append(v2)
#         graph[v2].append(v1)
        

#     for i in range(1,n+1):
#         visited = [False]*(n+1)
#         visited[i] = True 
#         result = bfs(i,visited,graph)
#         if abs(result-(n-result)) < answer:
#             answer = result 
#     return answer


from collections import deque
def bfs(start,visitied,graph):
    queue = deque([start])
    result = 1
    visitied[start] = True
    while queue:
        now = queue.popleft()
        
        for i in graph[now]:
            if visitied[i] == False:
                result += 1
                queue.append(i)
                visitied[i] = True
                
    return result
        

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+2)]
    
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
            
    for start,not_visit in wires:
        visitied = [False]*(n+2)
        visitied[not_visit] = True
        result = bfs(start,visitied,graph)
        if abs(result - (n-result)) < answer:
            answer = abs(result - (n-result))
        
    return answer

nj = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(8,nj))