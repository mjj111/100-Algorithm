def ten_to_two(x, n):
    rev = ''
    
    while x > 0:
        x, mod = divmod(x, 2)
        rev += str(mod)
    
    if len(rev) < n:
        while len(rev) < n:
            rev += '0'
    
    return rev[::-1]
        

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(0, n):
        a = arr1[i] | arr2[i]
        print(a)
        x = ten_to_two(a, n)
        result = ""
        for i in range(0, n):
            if x[i] == '1':
                result += "#"
            else:
                result += " "
        answer.append(result)    
    return answer

#&	and의 연산을 비트단위로 합니다.
#|	or의 연산을  비트단위로 합니다.
#^	xor의 연산을 비트단위로 합니다.
#~	not의 연산을 비트단위로 합니다.
#<<	비트단위로 "왼쪽으로 비트단위 밀기" 연산을 합니다.
#>>	비트단위로 "오른쪽으로 비트단위 밀기" 연산을 합니다.