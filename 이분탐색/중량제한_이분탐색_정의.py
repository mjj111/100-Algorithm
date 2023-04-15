import sys
sys.setrecursionlimit(1000000)

#weight로 cur부터 end 까지 갈 수 있나요? 
def can_go_to_end(cur, weight):
    global end
    if cur == end:
        return True

    for node, bridgeW in graph[cur]:
        if bridgeW >= weight and not visited[node]:  
            visited[node] = True
            
            #다음 노드로도 가보겠습니다. 
            if can_go_to_end(node, weight):
                return True 
    return False


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int, input().split())

left = 1
right = 10
while left <= right:
    mid = (left + right) // 2
    visited = [False] * (n + 1)
    visited[start] = True
    
    #가능하데 값 올려 
    if can_go_to_end(start, mid):
        left = mid + 1
    else:
        right  = mid - 1

print(right)


# 이분 탐색을 통해 특정 조건에 대해 최대 값을 찾는 경우 
# 왼쪽부터 나열된 정답들인지 -> 최대 
# 오른쪽부터 나열된 정답들인지 -> 최소 
# 에 따라 최대 최소로 계산할 수 있다.  

#안될 경우에 대해서는 그냥, 그래프 탐색 돌려라.