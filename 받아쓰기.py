s = "1451232125"
N = 2 
def solution(s, N):
    answer = 0
    result = set()
    for i in range(len(s)-N):
        tmp_s = s[i:i+N]
        flag = 0
        for i in range(1,N+1):
            if not str(i) in tmp_s:
                flag = 1
        if flag == 0:
            result.add(int(tmp_s))
    if not result:
        return -1
    return max(result)


print(solution(s,N))