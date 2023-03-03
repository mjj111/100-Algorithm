def solution(phone_book):
    len_number = [[] for _ in range(21)]
    answer = True
    for number in phone_book:
        len_number[len(number)].append(number) 
    for i in range(1,21):
        for str1 in len_number[i]:
            for j in range(i+1,21):
                for str2 in len_number[j]:
                    if str1 == str2[:i]:
                        return False
    return True