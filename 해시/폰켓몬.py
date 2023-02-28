def solution(nums):
    answer = 0
    set_nums = set(nums)
    how_many_animals = len(nums)
    can_get_num = how_many_animals / 2 
    
    if can_get_num < len(set_nums):
        return can_get_num
    else :
        return len(set_nums)
