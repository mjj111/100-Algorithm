answer = 0
n = 0
numberss = []
def dfs(idx, result,target):
    global answer 
    if idx == n:
        if result == target:
            answer += 1
        return
    else:
        dfs(idx+1, result+numberss[idx],target)
        dfs(idx+1, result-numberss[idx],target)
def solution(numbers, target):
    global n,numberss 
    numberss = numbers
    n = len(numbers)
    dfs(0,0,target)
    return answer