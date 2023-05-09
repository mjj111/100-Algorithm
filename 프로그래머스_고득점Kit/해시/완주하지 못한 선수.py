from collections import defaultdict
def solution(participant, completion):
    dic = defaultdict(int)
    for i in participant:
        dic[i] += 1 
    for j in completion:
        dic[j] -= 1
    for i in dic.keys():
        if dic[i] == 1:
            return i
