def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
    return "".join(s)

#chr() 함수는 숫자를 인자로 주면 아스키 코드에 해당하는 문자를 반환하며 (아스키 코드 -> 문자)
#ord() 함수는 문자의 아스키 코드를 반환한다. (문자 -> 아스키 코드)

 