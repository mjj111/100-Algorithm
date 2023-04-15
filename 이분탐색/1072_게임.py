x,y = map(int,input().split())
w = y*100//x
left, right = 1, 1000000000
result = 0
if w >=99:
    print(-1)
else:
    while left<=right:
        mid = (left+right)//2
        yy,xx = y + mid, x + mid
        #mid 가 커질 수록 승률이 상승한다. 
        
        if yy*100//xx > w:
            right = mid -1
        else:
            left = mid + 1
    print(left)
    