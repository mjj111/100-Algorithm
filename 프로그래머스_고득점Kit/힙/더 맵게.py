from heapq import heappush, heappop,heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while True:
        answer+=1
        a = heappop(scoville)
        if a < K :
            if scoville:
                b = heappop(scoville)
                heappush(scoville,a+(b*2))
            else:
                return -1
        else: return answer -1