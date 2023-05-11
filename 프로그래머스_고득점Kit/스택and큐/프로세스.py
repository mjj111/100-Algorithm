from collections import deque
def solution(priorities, location):
    p_list = deque()
    
    for i,j in enumerate(priorities):
        p_list.append((i,j))
    
    priorities.sort()
    
    time = 1
    while (p_list):
        now_location, now_process = p_list.popleft()
        maximum = priorities[-1]
        if now_process >= maximum:
            if now_location == location:
                return time
            else : 
                priorities.pop()
                time+=1
                continue
        else:
            p_list.append((now_location,now_process))
    
print(solution([1, 1, 9, 1, 1, 1],0))
# 1 3 2 2
# 3 2 2
# 2 2 3
# 2 3
# 3
