def solution(s):
    stack = []
    for i in s:
        if i == '(':  
            stack.append(i)
        else:  
            if not stack: 
                return False
            else:
                stack.pop() 
    
    return False if stack else True

(2)
def solution(s):
    stack  = []
    for i in s :
        if stack and stack[-1] =='(' and i == ')':
            stack.pop()
        else:
            stack.append(i)
            
    if stack :
        return False 
    return True