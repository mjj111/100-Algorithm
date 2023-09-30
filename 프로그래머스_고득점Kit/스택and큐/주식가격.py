
from collections import deque 
def solution(prices):
    answer = []
    deq = deque(prices)
    
    while deq:
        price = deq.popleft()
        sec = 0 
        for q in deq:
            sec +=1
            if price > q:
                break
        answer.append(sec)
        
    return answer