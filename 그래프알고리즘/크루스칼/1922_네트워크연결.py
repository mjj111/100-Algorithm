import sys 
input = sys.stdin.readline

#크루스칼 알고리즘
#유니온 파인드 

def find(a):
    if a == parent[a]:
        return a
    parent = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

        
        
n = int(input())
m = int(input())
arr = []
parent = [ i for i in range(n+1)]
res = 0

for i in range(m):
    a,b,c = map(int, input().split())
    arr.append( (c,a,b))
    
arr.sort(key = lambda x : x[0])
for dis, a, b, in arr:
    if find(a) != find(b):
        union(a,b)
        res += dis 
print(res)