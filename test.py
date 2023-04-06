select, answer, num_str,num1,num2 = 0,0,',0',0,0
select = int(input("1. 입력한 수식 계산하기 2. 두 수 사이의 합계:"))

if select == 1 :
    num_str = input("수식을 입력하시오")
    answer = eval(num_str)
    print("%s 결과는 %5.1f 입니다."%(num_str,answer))
    
elif select == 2:
    num1 = int(input("첫 번째 수를 입력하시오. :"))
    num2 = int(input("두 번째 수를 입력하시오. :"))
    for i in range(num1,num2 + 1, 1):
        answer +=i
    print("%d + ... %d는 %d입니다."%(num1,num2,answer))
else:
    print("1 혹은 2만 입력해주세요. ")
