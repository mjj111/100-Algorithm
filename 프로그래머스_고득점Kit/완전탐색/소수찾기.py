def solution(numbers):
    answer = 0
    
    def dfs(word):
        if len(word) == i:
            result.append(word)
            return 
        
        for j in range(len(numbers)):
            if chk[j] == False:
                chk[j] = True
                dfs(word + numbers[j])
                chk[j] = False
            
        
    numbers = list(numbers)
    chk = [False] * (len(numbers) + 1)
    result = []
    for i in range(1, len(numbers) + 1):
        dfs("")
        
    result = list(set(map(int, result)))
        
    for num in result:
        if num == 1 or num == 0:
            continue
            
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            answer += 1
            
    return answer
print(solution('17'))