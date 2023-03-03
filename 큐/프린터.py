from collections import deque
def solution(priorities, location):
    d = [0]*11 #우선 순순위 인덱스를 가진 값들의 개수 
    queue = deque()
    for i,p in enumerate(priorities):
        d[p] += 1
        queue.append((i,p))
    
    idx = 0
    while True:
        i,j = queue.popleft()
        if sum(d[j+1:])>0:
            queue.append((i,j))
        elif i == location:
            return idx+1
        else:
            idx += 1
            d[j] -= 1