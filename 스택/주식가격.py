def solution(prices):
    answer = [len(prices)-i-1 for i in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]:
                answer[i] = j-i
                break
    return answer