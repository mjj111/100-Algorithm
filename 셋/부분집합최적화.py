#A가 B의 부분집합인지 검사하는 3가지 이상의 방법 
#1. 이중 반복문을 통한 O(n**2) 시간복잡도를 가지는 접근방법
def is_subset(A,B):
    for a in A:
        for b in B:
            if a != b:
                return False
    return True 

#2. A와B를 정렬하여 이분탐색으로 부분집합인지 확인하는 
# n>m이 더 크다는 가정하에, 시간복잡도 O(mlogn)를 가지는 접근방법
def is_subset(A,B):
    A.sort()
    B.sort()
    
    def is_included_(element,tmp_list):
        right = len(tmp_list)
        left = 0
        mid = (right + left )// 2 
        while(right>=left):
            mid = (right + left )// 2 
            if element == tmp_list[mid] :
                return True 
            elif element >tmp_list[mid]:
                right = mid + 1
            else:
                left = mid - 1 
        return False 
    
    for a in A:
        if not (is_included_(a,B)):
            return False 
    return True 

#3. 해시를 사용하여, A와 B 집합에 대해 키 값으로 넣어준다. 
# value에 대해서는 넣어질 때마다 1씩 count를 올려준다. 

from collections import defaultdict
def is_subset(A,B):
    hash_table = defaultdict(int)
    for a in A:
        hash_table[a] = hash_table[a] + 1 
    
    for b in B:
        if not(hash_table[b]== 1):
            return False         
    return True 
                