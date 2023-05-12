def solution(array, commands):
    answer = []
    for i,j,idx in commands:
        answer.append(sorted(array[i-1:j])[idx-1])
    return answer