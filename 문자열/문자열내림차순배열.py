def solution(s):
    s = list(s)
    print(s)
    s.sort()#대문자는 소문자 보다 작은 문자다. 
    print(s) 
    s.sort(reverse = True )
    print(s) 
    return (''.join(s))