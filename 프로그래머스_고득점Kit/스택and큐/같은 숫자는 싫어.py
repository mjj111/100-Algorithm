def solution(s):
    result = []
    for i in s:
        if result and result[-1] == i:
            continue
        else : result.append(i)
    return result