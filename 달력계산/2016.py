#윤년은 2월이 29일까지 있는 날이다. 보통 28일이다. 
def solution(a, b):
    answer = 0
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    months = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
    for i in range(a-1):
         answer += months[i]
    answer += b-1 # 현재일에서 1일을 더해져있기 때문 (1월 0일부터 시작하지 않았다.) 혹은 answer을 1로 시작했어야했다. 
    answer = answer%7 
    
    return days[answer]