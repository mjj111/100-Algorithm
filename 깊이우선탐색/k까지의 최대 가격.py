n = int(input())
sales = [0] + list(map(int,input().split()))
result = []
def find_max_value(value,leaving):
    if leaving == 0:
        return result.append(value)
    elif leaving <0:
        return
    else:
        for i in range(n):
            find_max_value(value + sales[i+1] ,leaving - (i+1))
find_max_value(0,n)
print(max(result))