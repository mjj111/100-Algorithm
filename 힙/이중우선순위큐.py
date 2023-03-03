import heapq
def solution(operations):
    minq = []
    maxq = []
    removed = set()
    for oper in operations:
        op,digit = oper.split(" ")
        digit = int(digit)
        if op == "I":
            heapq.heappush(minq,digit)
            heapq.heappush(maxq,-digit)
        elif digit == -1 and minq:
            temp = heapq.heappop(minq)
            while temp in removed and minq:
                temp = heapq.heappop(minq)
            removed.add(temp)
        elif digit == 1 and maxq:
            temp = -heapq.heappop(maxq)
            while temp in removed and maxq:
                temp = -heapq.heappop(maxq)
            removed.add(temp)
    
    maxval = 0
    minval = 0
    while maxq:
        temp = -heapq.heappop(maxq)
        if temp not in removed:
            maxval = temp
            break
    
    while minq:
        temp = heapq.heappop(minq)
        if temp not in removed:
            minval = temp
            break
            
    return [maxval,minval]