def solution(s):
    a = []
    for i in s:
        print(a[-1:])
        if a[-1:] == [i]: 
            continue
        a.append(i)
    return a

# a[-1:] 는 마지막 인덱스 값 혹은 아무것도 없는 리스트를 반환한다. 가히 천재..
