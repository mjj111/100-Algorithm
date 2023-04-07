import sys 
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    li = list(map(int,input().split()))
    graph.append(li)
start_x, start_y = map(int,input().split())
end_x, end_y = map(int,input().split())
find = 0
visited = list([True]*(n) for i in range(n))
visited[start_x][start_y] = False
#초기화 완료 


def find_recursion(visited_tmp,x,y):
    global end_x
    global end_y
    global find
    global graph
    
    #Base Case 
    if x == end_x and y == end_y:
        find = 1
        return 
    
    #Search 
    #수평조사 
    flag = 0
    for i in range(y+1,n):
        #현재위치 y 보다 오른쪽에 벽이 있다면 
        if flag == 1:
            break
        if graph[x][i]== 1 :
            #오른쪽에서 찾는다.
            for j in range(i+1,n): 
                if graph[x][j] == 1 :
                    flag = 1
                    break
                #만약 오른쪽에 빈공간, 방문하지않은 곳이라면 
                elif graph[x][j] == 0 and visited_tmp[x][j] == True:
                    #방문 처리 
                    visited_tmp[x][j] = False
                    #다음 위치로 이동 
                    find_recursion(visited_tmp,x,j)
    flag = 0
    for i in range(y-1,-1,-1):
        #현재위치 y보다 왼쪽에 있다면
        if flag == 1:
            break
        if graph[x][i]== 1 :
            #왼쪽에서 찾는다.
            for j in range(i-1,-1,-1):
                if graph[x][j] == 1:
                    flag = 1
                    break
                #만약 왼쪽쪽에 빈공간, 방문하지않은 곳이라면 이동 
                elif graph[x][j] == 0 and visited_tmp[x][j] == True:
                    visited_tmp[x][j] = False
                    find_recursion(visited_tmp,x,j)
                    
    flag = 0
    #수직조사                    
    for i in range(x+1,n):
        #현재위치 x 보다 아래쪽에 있다면
        if flag == 1:
            break
        if graph[i][y]== 1 and i > x :
            #오른쪽에서 찾는다.
            for j in range(i+1,n):
                if graph[j][y] == 1:
                    flag = 1
                    break
                #만약 오른쪽에 빈공간, 방문하지않은 곳이라면 이동 
                elif graph[j][y] == 0 and visited_tmp[j][y] == True:
                    visited_tmp[j][y] = False
                    find_recursion(visited_tmp,j,y)
                    
    flag = 0                
    for i in range(x-1,-1,-1):
        #현재위치 x 보다 아래쪽에 있다면
        if flag == 1:
            break
        if graph[i][y]== 1 and i < x :
            #오른쪽에서 찾는다.
            for j in range(i-1,-1,-1):
                if graph[j][y] == 1:
                    flag = 1
                    break
                #만약 오른쪽에 빈공간, 방문하지않은 곳이라면 이동 
                elif graph[j][y] == 0 and visited_tmp[j][y] == True:
                    visited_tmp[j][y] = False
                    find_recursion(visited_tmp,j,y)

find_recursion(visited,start_x,start_y)

if find == 0:
    print("NO")
elif find == 1 :
    print("YES")


