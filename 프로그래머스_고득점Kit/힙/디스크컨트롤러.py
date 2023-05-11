from heapq import heapify , heappush, heappop 
def solution(jobs):
    total,now,start = 0,0,-1
    work = [] 
    done =  0
    
    while done <len(jobs):
        #일할 것이 없다면 가능한 일들을 일단 넣는다. 노동 시간 우선순위로  
        for request,work_time in jobs:
            if start < request <=now :
                heappush(work,(work_time,request))
    
        if work :
            work_time,request = heappop(work)
            done+=1
            start = now 
            now += work_time 
            total += now - request
        else: 
            now +=1
    return total // len(jobs)

