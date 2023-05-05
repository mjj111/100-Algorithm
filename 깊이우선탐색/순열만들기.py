a = [1,2,3,4,5,6]
wanna_len = 3
result  = []
def get_permutaion_start(n,index,arr):
    if n == wanna_len:
        return result.append(','.join(map(str,arr)))
    
    for i in range(index+1,len(a)):
        arr.append(a[i])
        get_permutaion_start(n+1,i,arr)
        arr.pop()
        
for i in range(len(a)):
    tmp_result = []
    get_permutaion_start(0,i-1,tmp_result)
print(result)