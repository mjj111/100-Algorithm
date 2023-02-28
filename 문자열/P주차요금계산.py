import math
def solution(fees, records):
    def get_fee(minutes, fees):
        return fees[1] + math.ceil(max(0, (minutes - fees[0])) / fees[2]) * fees[3]
# Math.ceil 은 소수값이 존재할 때 값을 올리는 역활을 하는 함수이며,
# Math.floor 는 소수값이 존재할 때 소수값을 버리는 역활을 하는 함수이며,
# Math.round 는 소수값에 따라 올리거나 버리는 역활을 하는 반올림 함수입니다.
   
    parking = dict()
    stack = dict()
    
    for record in records:
        time, car, cmd = record.split()
        hour, minute = time.split(":")
        minutes = int(hour) * 60 + int(minute) # 시간 -> 분 환산

        if cmd == 'IN':
            parking[car] = minutes
        elif cmd == 'OUT':
            try:
                stack[car] += minutes - parking[car]
            except:
                stack[car] = minutes - parking[car]
            del parking[car] # 출차 차량 삭제
    
    # 출차 기록 없는 차 23:59 출차 처리
    for car, minute in parking.items():
        try:
            stack[car] += 23*60+59 - minute
        except:
            stack[car] = 23*60+59 - minute
        
    return [get_fee(time, fees) for car, time in sorted(list(stack.items()), key=lambda x: x[0])]