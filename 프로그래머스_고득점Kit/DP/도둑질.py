#첫번째 집과 마지막 집도 연결될 수 있다. -> 원형이기 때문에 
#첫번째 집을 무조건 터는 경우와 마지막 집을 무조건 터는 경우를 나눠야한다. 
def solution(money):
    dp = [0] * len(money)
    dp[0], dp[1] = money[0], max(money[0], money[1])
    
    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])

    pre = max(dp)
    
    dp = [0] * len(money)
    dp[0], dp[1] = 0, money[1]
    for i in range(2, len(money)):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])

    return max(pre,max(dp))
