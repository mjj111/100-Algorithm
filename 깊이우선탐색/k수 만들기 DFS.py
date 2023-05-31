result = []
def make_k(k,now,try_num):
    if now == k:
        return result.append(try_num)
    elif now >k:
        return 
    else:
        make_k(k,now + 1, try_num+1)
        if now != 0 :
            make_k(k,now *2 ,try_num+1)
k = int(input())
make_k(k,0,0)
print(min(result))
