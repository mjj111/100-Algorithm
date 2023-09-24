# 재귀 함수로 구현한 이진탐색 
def recursion_binary_search(array, target, start, end):
    if start > end:
        return 
    mid = (start + end)//2
    
    if array[mid] == target:
        return mid 
    elif array[mid] > target:
        return recursion_binary_search(array,target,start,mid-1)
    else:
        return recursion_binary_search(array,target, mid +1 ,end)
   
    
# 반복문으로 구현한 이진 탐색 
def repeat_binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid 
        elif array[mid] > target:
            end = mid -1 
        else :
            start = mid + 1 
    return 


#target과 같지만 왼쪽에 존재 하는 것 
# lower_bound 
def lower_bound(data, target):
    low = 0
    high = len(data)
    while low < high:
        mid = (low + high)//2
        if data[mid] >= target:
            high = mid -1 
        else :
            low = mid +1
    return low 


#target과 같지만 오른쪽에 존재하는 것 
#upper_bound
def upper_bound(data,target):
    low = 0 
    high = len(data)
    while low < high:
        mid = (low + high)//2
        if data[mid] >= target:
            high = mid -1 
        else :
            low = mid +1
    return high


# 매개변수 탐색 
#조건 lo + 1 < hi 
#반복문 내에서 array[low] < array[high]가 항상 성립한다.
def paprameter_binary_search(array,high,low,value):
    while low +1 < high :
        mid = (low + high) // 2 
        if find[array[mid]] <= value:
            low = mid
        else:
            high = mid 
    return array[low]

def find(param):
    pass # 어떤 조건을 만족하면 true 아니라면 false 를 반환하도록 구현 


 
