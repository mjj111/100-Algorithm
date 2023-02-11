import sys
from collections import deque
input = sys.stdin.readline
t= int(input())
move_x = [1,-1,0,0]
move_y = [0,0,-1,1]


def bfs(x,y):
    deq = deque()
    deq.append([x,y])
    while deq:
        now_x, now_y = deq.popleft()
        for i in range(4):
            next_x = now_x + move_x[i]
            next_y = now_y + move_y[i]
            if 0<= next_x <column and 0<= next_y < row and procession[next_x][next_y] == 1:
                procession[next_x][next_y] = 0
                deq.append([next_x,next_y])


for i in range(t):
    column,row,case = map(int, input().split())
    procession  = list([0] * row for i in range(column)) #[[0] * m for i in range(n)]
    result = 0
    for i in range(case):
        a, b = map(int,input().split())
        procession[a][b] = 1
    for c in range(column):
        for r in range(row):
            if procession[c][r] == 1:
                bfs(c,r)
                procession [c][r] = 0
                result +=1 
    print(result)

