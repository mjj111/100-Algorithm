def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i] == phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                return False
    return True

(2)
from collections import defaultdict
def solution(phone_book):
    dic = defaultdict(int)
    phone_book.sort(key = lambda x : len(x))
    for number in phone_book:
        tmp = ""
        for i_number in  [x for x in number]:
            tmp = tmp + i_number
            if dic[tmp] == 1 :
                return False
        dic[number] += 1 
    return True
            