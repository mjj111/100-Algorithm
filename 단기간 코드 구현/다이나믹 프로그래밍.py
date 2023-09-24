#bottom-up 
#작은 문제부터 풀고 올라간다. 
def fibo_bottom_up(n):
    if n <= 1 :
        return n
    first = 0
    second = 1
    next = 0 
    for i in range(n):
        next = first + second
        first = second
        second = next 
    return next 

#top-down 
#큰 문제를 풀 때, 작은 문제가 아직 풀리지 않은 경우, 그제서야 작은 문제를 해결한다. 
def fibo_top_down(n):
    if memo[n] > 0:
        return memo[n]
    if n <= 1:
        return memo[n]
    else:
        memo[n] = fibo_top_down(n-1) + fibo_top_down(n-2)
        return memo[n]
memo = [0] * 100 
memo[1] = 1