#오른쪽부터 deliveries와 pickups 값을 조회하여 0이 아닌 지점을 찾는다. // 해당 지점까지 움직일 것이다. 
# 목표지부터 출발점까지 조회하여 deliveries 최대값을 가져온다. // deliveries없앤다
# 목표지부터 출발점까지 조회하여 pickups 최대 값을 가져온다. // pickups없앤다.
#위의 과정을 반복  while deliveries or pickups :
def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups :
        deliver_cap, pickup_cap = cap, cap
        while deliveries and deliveries[-1] == 0 :
            deliveries.pop()
        while pickups and pickups[-1] == 0 :
            pickups.pop()
        answer += max(len(deliveries), len(pickups))*2
        
        
        
        while deliveries and deliver_cap > 0:
            box = deliveries.pop()
            if box <= deliver_cap :
                deliver_cap -= box
            else :
                deliveries.append(box - deliver_cap)
                break
                
        while pickups and pickup_cap > 0 :
            box = pickups.pop()
            if box <= pickup_cap :
                pickup_cap -= box
            else :
                pickups.append(box - pickup_cap)
                break
        
    return answer