from collections import deque
def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    wait = deque()
    sum_weight = 0
    time = 0
    while trucks:
        time += 1
        while wait and wait[0][0] <= time:
            t,w = wait.popleft()
            sum_weight -= w
        if sum_weight+trucks[0] <= weight:
            truck = trucks.popleft()
            wait.append((bridge_length+time,truck))
            sum_weight += truck
    return wait[-1][0]