k = int(input())
result = []
def make_k(k,arr):
    now = sum(arr)
    if now == k :
        result.append(arr)
    elif now > k:
        return
    else:
        make_k(k,arr + [1])
        make_k(k,arr + [2])
        make_k(k,arr + [3])
tmp_list = []
make_k(k,tmp_list)
for i in result:
    print(" + ".join(map(str,i)))        
print(len(result))