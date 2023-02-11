import sys
input = sys.stdin.readline
n,wannaget = map(int, input().split())
trees = list(map(int,input().split()))

def cutting_tree(center):
    sum_log = 0
    for tree in trees:
        if tree >= center:
            sum_log += tree - center
    return sum_log

left = 0
right = max(trees)
result = 0

while left <= right:
    mid = (left+right)//2
    sum_of_log = cutting_tree(mid) 
    if sum_of_log >= wannaget:
        if result<mid:
            result = mid
        left = mid +1
    else:
        right = mid - 1
print(result)