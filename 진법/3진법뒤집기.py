def solution(n):
    answer = ''
    while n > 0:			
        n, re=divmod(n,3)	# n을 3으로 나눈 몫과 나머지
        answer+=str(re)
         
    return int(answer, 3)	# 3진법 answer을 10진법으로 변환코드를 입력하세요