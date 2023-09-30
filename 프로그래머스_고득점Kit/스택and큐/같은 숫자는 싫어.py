def solution(s):
    result = []
    for i in s:
        if result and result[-1] == i:
            continue
        else : result.append(i)
    return result

'''0-9까지의 숫자 배열 
연속적인 같은 숫자는 하나만 남기고 전부 제거 
만난 숫자에 dq가 비었다면 그냥 추가
만난 숫자와 dq의 최상단과 같다면 그냥 지나가 
만난 숫자와 dq의 최상단이 다르다면 dq에 추가 
'''
from collections import deque
def solution(arr):
    dq = deque()
    for i in arr:
        if not dq:
            dq.append(i)
            continue 
        top = dq.pop()
        if i == top:
            dq.append(i)
            continue
        else: 
            dq.append(top)
            dq.append(i)
    return list(dq)