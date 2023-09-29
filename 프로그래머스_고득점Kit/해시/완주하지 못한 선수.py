from collections import defaultdict
def solution(participant, completion):
    dic = defaultdict(int)
    for i in participant:
        dic[i] += 1 
    for i in completion:
        dic[i] -= 1
    for key,value in dic.items():
        if value == 1:
            return key
