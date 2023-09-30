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

(2)
from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    time = 1 
    bridge =deque()
    bridge.append([truck_weights.popleft(),1])
    while(bridge or truck_weights):
        time +=1 
        if bridge:
            if bridge[0][1] + 1 > bridge_length:
                bridge.popleft()

            if truck_weights:
                total_weight = 0
                for truck in bridge:
                    truck[1] += 1
                    total_weight += truck[0]
                if total_weight + truck_weights[0] <= weight:
                    bridge.append([truck_weights.popleft(),1])
            else:
                for truck in bridge:
                    truck[1] += 1
        else: 
            bridge.append([truck_weights.popleft(),1])
    return time