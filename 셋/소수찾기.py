def solution(n):
    	# 2부터 n까지의 숫자 배열 만들기
    num_set = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num_set: # 배수 제거
            num_set -= set(range(i*2, n+1, i))

    return len(num_set)

#리스트간의 뺴기와 더하기가 불가능하지만 set의 경우 가능하다 .


a = set([1,2,3])
b= set([1])
a-= b
print (a)


print(set(range(1,10)))

tmp_a = [1,2,3]
tmp_b = [1]
a -= b
print(a)

tmp_aa = [1,2,3]
print(tmp_a)