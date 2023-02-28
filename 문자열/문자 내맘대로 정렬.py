def solution(strings, n):
    strings.sort(key=lambda x : (x[n],x))
    return strings

#sort(key= lambda x :)를 사용하며 안에 튜플을 사용하게 되면 우선순위를 부여할 수 있다 .