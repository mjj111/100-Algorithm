#처음 문제를 접근할 때 크기를 비교해야한다.
#단순히 주어진 다리 n개를 없애려고했다.
#그러나, 없애려고하는 다리의 개수가 50,000개 이하였다.
# 즉, 50000개 중에 3개를 없앤다고 하면 경우의 수가 50000 * 49999 * 49998 인 것이다..
# 거리의 최솟값에 따라 필요없는 연산을 빼는 형식으로 
#n log n 밖에 없다 -> 이분탐색 

import sys
def solution(distance, rocks, n):
    answer = 0
    left, right = 0, distance
    rocks.append(distance) 
    rocks.sort()
    
    while left <= right:
        mid = (left + right) // 2 
        current, remove =  0, 0 
        
        # 거리 구하기
        for rock in rocks:
            dis = rock - current
            if dis < mid: 
                remove += 1
            else:
                current = rock
                
        if remove > n: 
            right = mid - 1
        else: 
            left = mid + 1
        
    return right