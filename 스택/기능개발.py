def solution(progresses, speeds):
    # remove가 pop보다 빠르다 ㅋ 
    answer = []
    time = 1
    complete = 0
    while len(speeds)>0:#progresses, speeds [0]을 다 없앨 것이다.
        if progresses[0] + time * speeds[0] >=100:
            complete +=1
            progresses.remove(progresses[0])
            speeds.remove(speeds[0])
            if len(speeds) == 0:
                answer.append(complete)
                return answer
        else:# 현재 녀석은 아직인데 
            if complete > 0: # 만약 이미 털린 앞에 녀석들이 존재할 경우
                answer.append(complete)
                complete = 0
            time+=1
    return answer