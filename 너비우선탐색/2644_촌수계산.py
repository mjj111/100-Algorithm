import sys
from collections import deque

def bfs(x):
    deq = deque()
    deq.append(x)
    visited[x] = 1
    result = 0
    while deq:
        result +=1
        for _ in range(len(deq)):
            now_x = deq.popleft()
            if now_x == wanna_find_y:
                return result -1
            for next_x in people[now_x]:
                if visited[next_x] == 0:
                    visited[next_x] = 1
                    deq.append(next_x)
    return -1


howmany_people = int(input())
wanna_find_x,wanna_find_y = map(int, input().split())
relation = int(input())
people = [[] for _ in range(howmany_people+1)] # 빈2차원 행렬을 만들기 위해서 사용 
for i in range(relation):
    x,y = map(int, input().split())
    people[x].append(y)
    people[y].append(x)# 단방향이라면 넣지 않아도 된다
    
visited = [0] * (howmany_people + 1) # 빈 1차원 행렬을 만들기 위해 사용 
print(bfs(wanna_find_x))