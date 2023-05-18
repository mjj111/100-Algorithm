def solution(people, limit):
    answer,left,right = 0,0,len(people) -1
    people.sort()
    
    while(left <= right):
        answer+=1 
        if people[left]+people[right] <=limit:
            left +=1 # 가능하다?! 작은 녀석 추가!
        right -=1#안되더라도 무거운 녀석은 보낸다. 
    return answer