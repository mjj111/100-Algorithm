from collections import defaultdict
def solution(clothes):
    d = defaultdict(int)
    for name,item in clothes:
        d[item] += 1
    
    answer = 1
    for item,n in d.items():
        answer *= (n+1)
    return answer-1