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
    
(2)
'''특정 프로세스가 몇 번째로 실행되는지
 대기중인 프로세스 하나를 꺼냅니다.
 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.(실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.)
 
'''

from collections import deque
def solution(priorities, location):
    priorities = deque(priorities)
    idx =  deque([x for x in range(len(priorities))])
    count = 0 
    while(priorities):
        first_need = max(priorities) 
        now = priorities.popleft() 
        now_idx = idx.popleft()     
            
        if now == first_need :
            count += 1
            if now_idx == location:
                 return count
        else:
            priorities.append(now)
            idx.append(now_idx)     
        
