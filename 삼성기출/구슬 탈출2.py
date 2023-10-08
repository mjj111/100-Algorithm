'''세로 크기는 N, 가로 크기는 M
파란 구슬이 구멍에 들어가면 안 된다.
빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 
빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다
빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다
빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다
기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지

두공의 위치가 동일한 경우는 이미 했던 행위다. (break 지점)

전략 

네가지 방향에 대해 미리 변수 선언해준다. (왼쪽 ,오른쪽 ,위,아래)
두 공의 위치를 가진 visited를 선언한다.
[[1][2][3][4]] 1,2  3,4 파란색 빨간색 공 위치 
visited = [[0]* max(m,n) for _ in range(4)]
-------------------------------------------

네 방향에 대해 빨간색공, 파란색공 위치, depth와 visited를 가지고 반복한다.
만약 depth가 10을 초과한다면 break 

받은 방향에 대해서 현재 파란색,빨간색 공의 위치를 움직인다 (move 작성) 위치 return 
    벽에서만나는 경우, 끝까지의 거리가 긴 공이 끝에서 한칸 뒤로 간다. 
                        짧은 녀석은 끝까지 이동한다. 
    만약 빨간색공이 빠지고 파란색 공도 빠진다면 [-1,-1,-1,-1] 반환
    만약 빨간색공이 빠지고 파란색 공이 안빠진다면 [max_int,max_int,max_int,max_int] 반환
    
move 의 결과에 따라 
    만약 
        이미 visited 된 곳이라면 넘어간다. 
        받은 값의 [0] 값이 -1이라면 넘어간다. 
    만약
        받은 값의 [0] 값이 max_int라면 정답을 갱신한다. answer = min(answer,depth)
    
    아니라면?
        depth 을 추가 하고 
        visited를 1로 갱신한 뒤에 
        다음으로 보낸다.   
'''
from collections import deque 
import sys
MAX_INT = sys.maxsize
answer = MAX_INT
n,m = map(int,input().split())
board = [[0]*m for _ in range(n)]
blue_x,blue_y = 0,0



# board와 빨간색공, 파란색공, 골인 위치 초기화 
for i in range(n):
    tmp = input()
    for j in range(m):
        board[i][j] = tmp[j]
        if tmp[j] == 'B':
            blue_x = i
            blue_y = j
        elif tmp[j] == 'R':
            red_x = i
            red_y = j

            
#각 공의 방문 초기화 
ball_location = [red_x,red_y,blue_x,blue_y]
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
# 기울기에 따른 이동방향 네가지 선언 
direction_x = [0,0,-1,1]
direction_y = [1,-1,0,0]



# n,m 크기 이내 판별 
def available_x_y(x,y):
    if  x < n and y < m and 0 < x and 0 < y :
        return True 
    else : 
        return False 
    

#네 방향에 대해 빨간색공, 파란색공 위치를 움직이고 
# 움직인 결과 위치를 반환한다.
# 빨간 공만 골인했을 경우 [max_int,max_int,max_int,max_int]
# 두 공 모두 골인했을 경우 [-1,-1,-1,-1]
# 이외는 결과 위치 반환 
def move(ball_location,direction_x,direction_y):
    now_red_x =ball_location[0]
    now_red_y =ball_location[1]
    now_blue_x =ball_location[2]
    now_blue_y = ball_location[3]
    red_length_run = 0
    blue_length_run = 0

    #빨간색 공 이동
    while(True):
        #board 이내 움직임이라면 
        if available_x_y(now_red_x + direction_x ,now_red_y +direction_y):
            
            #갈 수 있다면 
            if board[now_red_x + direction_x][now_red_y+ direction_y] == '.':
                now_red_x += direction_x
                now_red_y += direction_y
                red_length_run += 1 # 움직인 거리 상승 
                
            #벽이라면 
            elif board[now_red_x + direction_x][now_red_y+ direction_y] == '#':
                break 
            
            #골인 지점이라면 
            elif board[now_red_x + direction_x][now_red_y+ direction_y] == 'O':
                now_red_x = MAX_INT
                now_red_y = MAX_INT
                break
            
            else:
                now_red_x += direction_x
                now_red_y += direction_y
                red_length_run += 1 # 움직인 거리 상승 
        else:
            break
            
    #파란색 공 이동
    while(True):
        #board 이내 움직임이라면 
        if available_x_y(now_blue_x + direction_x ,now_blue_y+ direction_y):
            #갈 수 있다면 
            if board[now_blue_x + direction_x][now_blue_y+ direction_y] == '.':
                now_blue_x += direction_x
                now_blue_y += direction_y
                blue_length_run += 1 # 움직인 거리 상승 
            #벽이라면 
            elif board[now_blue_x + direction_x][now_blue_y+ direction_y] == '#':
                break 
            #골인 지점이라면 
            elif board[now_blue_x + direction_x][now_blue_y+ direction_y] == 'O':
                now_blue_x = MAX_INT
                now_blue_y = MAX_INT
                break
            else:
                now_blue_x += direction_x
                now_blue_y += direction_y
                blue_length_run += 1 # 움직인 거리 상승 
        else:
            break
            
    #만약 빨간색공이 빠지고 파란색 공도 빠진다면        
    if now_red_x == MAX_INT and now_blue_x == MAX_INT :
        return [-1,-1,-1,-1]
    
    #만약 빨간색공이 빠지고 파란색 공이 안빠진다면
    if now_red_x == MAX_INT and now_blue_x != MAX_INT :
        return  [MAX_INT,MAX_INT,MAX_INT,MAX_INT]
    
    else:
        #둘 다 동일 위치 라면 길게 움직인 녀석이 한 칸 뒤로 이동
        if now_red_x == now_blue_x and now_red_y == now_blue_y:
            if red_length_run > blue_length_run:
                now_red_x -= direction_x
                now_red_y -= direction_y
            else:
                now_blue_x -= direction_x
                now_blue_y -= direction_y
        return [now_red_x,now_red_y,now_blue_x,now_blue_y]
    
        
        
        
#네 방향에 대해 빨간색공, 파란색공 위치, depth와 visited를 가지고 반복한다.
def dfs(ball_location,visited,depth):
    global answer
    if depth > 10:
        return 
    for i in range(4):
        now_ball_location = move(ball_location,direction_x[i],direction_y[i])

        # 이미 방문한 케이스 
        if visited[now_ball_location[0]][now_ball_location[1]][now_ball_location[2]][now_ball_location[3]] == 1:
            continue 
        
        #성공 케이스 
        if now_ball_location[0] == 9223372036854775807: 
            answer = min(answer,depth)
            visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
            continue 
        
        # 실패 케이스 
        if now_ball_location[0] == -1:
            continue 
        
        
        else: #아직 이동 가능이라면 
            #방문 처리와 함께 다음으로 이동 
            visited[now_ball_location[0]][now_ball_location[1]][now_ball_location[2]][now_ball_location[3]] =1 
            dfs(now_ball_location,visited,depth+1)
        
    
dfs(ball_location,visited,1)
if answer == 9223372036854775807 :
    print(-1)
else:
    print(answer)


... 실패 


from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)] 
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)] # 4차원으로 만들어야했다. 
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()

def init():
    rx, ry, bx, by = [0] * 4
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R': 
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
    q.append((rx, ry, bx, by, 1)) 
    visited[rx][ry][bx][by] = True
    
def move(x, y, dx, dy): # 이동하는데 가볍게 구현해야했다. 많은 역할을 부여했다. (이동만 하도록 해야한다. )
    count = 0 
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count


def bfs():
    init() #초기화 
    while q: 
        rx, ry, bx, by, depth = q.popleft() 
        if depth > 10: 
            break
        for i in range(len(dx)): 
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i]) 
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i]) 
                        
            if board[next_bx][next_by] == 'O':  #파란구술이 떨어지는가 먼저 확인해야했다. 
                continue
            if board[next_rx][next_ry] == 'O': 
                print(depth)
                return
            if next_rx == next_bx and next_ry == next_by :
                if r_count > b_count: 
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]
                    
            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                q.append((next_rx, next_ry, next_bx, next_by, depth +1))
    print(-1) 

bfs()


'''                                                                    느낀점 
객체지향을 공부하면서 def로 나눠놓고 하나에 너무 많은 책임을 부여했다.
필요한 행위에 대해서 먼저 나누고, 
가장 큰 로직에서 작은 로직을 불러오도록 하자. (TDD할 때처럼 일단 임의의 값을 반환하도록 선언 후 구현 )
'''



'''                                                                고쳐야할 점

String을 나눌 때는 splie()이 아닌 strip()이다. 
input().strip()

차원 선언하는 방법이 서툴었다. 
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

'''