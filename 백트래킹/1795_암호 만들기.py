import sys
input = sys.stdin.readline
def back_tracking(now_len,idx) :
    if now_len == how_long_alpha:
        mo,ja = 0,0
        for i in range(how_long_alpha):
            if answer[i] in consonant:
                mo +=1 
            else:
                ja +=1
        if mo >= 1 and ja >= 2:
            print("".join(answer))
        return 
    for s in range(idx,how_many_possible_alpha):
        answer.append(words[s]) # 현재에 추가 
        back_tracking(now_len+1, s +1)# 다음 녀석으로 넘겨주고 
        answer.pop() #다시 리셋

how_long_alpha, how_many_possible_alpha= map(int,input().split())
words = sorted(list(map(str,input().split())))
consonant = ['a','e','i','o','u']
answer = []
back_tracking(0,0)

