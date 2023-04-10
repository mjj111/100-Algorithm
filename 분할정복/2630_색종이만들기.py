#문제 해석 : 종이를 4등분하여 분할된 정사각형 구역의 색종이가 모두 같은 색이라면 하나의 색종이로써 인식한다.
#           인식된 색종이는 흰색과 파란색으로 구분되며 각 색종이의 개수를 구하여라 

#문제 접근 : 종이를 4등분하여(divide)하여 접근 가능하다면(conquer) 색종이로 보고 아니라면 해당 구역을 다시 4등분하여 접근한다.
#           등분과 접근 가능이 깊이있게 반복한다. -> 재귀
#           재귀를 사용해서 등분하게되며, Base Case 로써 접근 가능을 조건을 두어 계산한다. 

#일반적인 분할정복 pseudo code 
#def f(x):
#    if f(x)가 계산가능하다면:
#        return f(x)를 계산한 값 # 정복
#    else:
#        x를 x1, x2로 분할
#        f(x1)과 f(x2) 호출 # 분할
#        return f(x1), f(x2)로 구한 값 # 조합
    
def initialize_n_and_colored_paper():
    n = int(input())
    for _ in range(n):
        color_paper.append(list(map(int,input().split())))

def square_colored_paper(papers):
    global white,blue
    paper_sum = 0

    for paper_row in papers:
        paper_sum += sum(paper_row)
        
    if paper_sum == 0: return 0
    elif paper_sum == len(papers)**2: return 1
    else : return 3
            

def find_the_number_of_white_confetti_and_blue_confetti(paper):
    global white,blue
    result = 0
    result  = square_colored_paper(paper)
    
    if not paper:
        return
    
    if result ==  0 :
        white +=1 
        print(paper)
        return 
    
    elif result == 1:
        blue +=1 
        print(paper)
        return 
        
        
     # 처음에 이렇게 4개로 2차원 리스트를 분할하려 했으나 생각대로 분할되지 않더군요! 그래서 dx,dy를 통해 새롭게 분할하게 되었습니다.     
    else : 
        find_the_number_of_white_confetti_and_blue_confetti(paper[:len(paper)//2][:len(paper)//2]) #1사분면 
        find_the_number_of_white_confetti_and_blue_confetti(paper[len(paper)//2:][:len(paper)//2]) #2사분면
        find_the_number_of_white_confetti_and_blue_confetti(paper[:len(paper)//2][len(paper)//2:]) #3사분면
        find_the_number_of_white_confetti_and_blue_confetti(paper[len(paper)//2:][len(paper)//2:]) #4사분면
        return 
        
n = 0
color_paper = []
initialize_n_and_colored_paper()


white = 0
blue = 0
find_the_number_of_white_confetti_and_blue_confetti(color_paper)
print(white)
print(blue)

