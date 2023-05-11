from collections import deque 
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    time = 0 
    bridge_sum = 0
    while(trucks):
        time +=1 
        now_truck = trucks[0]
        bridge_sum -= bridge.popleft()
        if bridge_sum + now_truck <= weight:
            bridge.append(now_truck)
            bridge_sum += now_truck
            trucks.popleft()
        else:
            bridge.append(0)
    return time + bridge_length
        