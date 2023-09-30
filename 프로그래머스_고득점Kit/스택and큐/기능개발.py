def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while progresses:
        if (progresses[0] + time*speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
     
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    
    return answer

(2)
''' 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
 개발속도는 모두 다르기에
뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포
진도가 적힌 정수 배열 progresses
 개발 속도가 적힌 정수 배열 speeds
  각 배포마다 몇 개의 기능이 배포되는지 return 
progresses 와 spedds를 데큐로 만든다. 

걸리는 날짜 선언 
진행과 스피드가 빌 때까지 반복 
진행과 스피드의 왼쪽을 뽑아서 100>= 을 넘길 때까지 날짜를 높힌다. 
100을 넘게되는 순간 다음 차례의 각 개발진행이 100이 넘는지 확인한다. 
100이 넘는 녀석들을 없애준다. 
없앨 때마다 얼마나 없애는지 계산하고 answer에 답을 추가한다. 
'''
from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    day = 1
    while(speeds):
        if progresses[0] + speeds[0] *day < 100: day+=1
            
        else:
            total = 0 
            for i in range(len(progresses)):
                if progresses[i] + speeds[i] *day >= 100:
                    total +=1 
                    
                else:
                    break
                    
            for i in range(total):
                progresses.popleft()
                speeds.popleft()
                
            answer.append(total)               
    return answer