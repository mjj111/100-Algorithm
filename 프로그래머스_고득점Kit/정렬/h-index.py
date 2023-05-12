#문제 해석 : 조건 1
#           n 편의 논문 중 h 번 이상 인용된 논문이 h 편 이상

#           조건 2
#           나머지 논문이 h번 이하 인용된 경우의 h 최대 값 구하기 

#           제한 사항 
#           n =  1~  1,000 ,논문별 인용 횟수는 0~ 10,000


#문제 접근 : 초기화를 위해 1,2를 수행한다.  (1. n의 수를 len 을 통해 구해놓는다.  2. 논문들을 내림차순으로 정렬한다.)
#           배열의 크기를 h의 최대값을 둘 수 있다. (n 편의 논문 중 h 번 이상 인용된 논문이 h 편 이상이기 때문에 h 는 n을 초과하지 못한다)  
#           큰 수부터 접근하여, 해당 인덱스는 인덱스 값보다 많이 인용된 논문의 수가 된다. 
#           인덱스 값보다 인덱스가 더 크다면, 인덱스는 h로써 조건을 충족하게된다. 

def solution(citations):
    citations.sort(reverse=True)    
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    return len(citations)

