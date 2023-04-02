import sys
import random
import time

#버블정렬
def buble_sort(numbers):
    for i in range(len(numbers), 1, -1):
        for j in range(i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

#선택정렬
def selection_sort(numbers):
    for i in range(len(numbers)):
        mn = sys.maxsize
        for j in range(i, len(numbers)):
            if numbers[j] < mn:
                mn = numbers[j]
                mn_idx = j
        numbers[i], numbers[mn_idx] = numbers[mn_idx], numbers[i]
    return numbers

#삽입정렬    
def insert_sort(numbers):
    for i in range(1, len(numbers)):
        target = numbers[i]
        for j in range(i, 0, -1):
            if numbers[j-1] > target:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            else:
                break
    return numbers

#합병정렬
def merge_sort(l):
    if len(l) < 2:
        return l

    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])

    if left and right:
        return merge(left, right)

def merge(left, right):
    left.append(99999)      # Suppose 99999 is infinite.
    right.append(99999)     # Suppose 99999 is infinite.
    index1 = 0
    index2 = 0
    temp = []

    while left[index1] != 99999 or right[index2] != 99999:
        if left[index1] >= right[index2]:
            temp.append(right[index2])
            index2 += 1
        else:
            temp.append(left[index1])
            index1 += 1
    return temp

#빠른정렬 //마지막 값을 피봇으로 선택 
def quick_sort_last(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[len(numbers)-1]
    left, right, equal = [], [], []
    for num in numbers:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    return quick_sort_last(left) + equal + quick_sort_last(right)


#빠른정렬 //중간 피봇
def quick_sort_middle(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[len(numbers)//2]
    left, right, equal = [], [], []
    for num in numbers:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    return quick_sort_middle(left) + equal + quick_sort_middle(right)

#빠른정렬 // 랜덤 피봇
def quick_sort_random(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[ random.randrange(0,len(numbers)-1)]
    left, right, equal = [], [], []
    for num in numbers:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    return quick_sort_random(left) + equal + quick_sort_random(right)


# 힙 정렬
def heapify(numbers, index, heap_size):
  largest = index
  left = 2 * index + 1
  right = 2 * index + 2
  
  if left < heap_size and numbers[right] > numbers[largest]:
    largest = left
    
  if right < heap_size and numbers[right] > numbers[largest]:
    largest = right
    
  if largest != index:
    numbers[largest], numbers[index] = numbers[index], numbers[largest]
    heapify(numbers, largest, heap_size)

def heap_sort(numbers):
  n = len(numbers)
  
  for i in range(n // 2 - 1, -1, -1):
    heapify(numbers, i, n)
    
  for i in range(n - 1, 0, -1):
    numbers[0], numbers[i] = numbers[i], numbers[0]
    heapify(numbers, 0, i)

  return numbers

#랜덤 숫자 초기화 
def get_numbers_n(n):
    cover_number = list(range(1,n))
    return random.sample(cover_number,len(cover_number))

#버블 정렬에따른 시간 추출 
def get_Nsize_average_time_with_buble_sort(nsize):
    result = []
    for i in range(10):
        numbers = get_numbers_n(nsize)
        start = time.time()
        # 알고리즘
        buble_sort(numbers)
        result.append(time.time() - start)
    return sum(result)/10

#선택 정렬에따른 시간 추출 
def get_Nsize_average_time_with_selection_sort(nsize):
    result = []
    for i in range(10):
        numbers = get_numbers_n(nsize)
        start = time.time()
        # 알고리즘
        selection_sort(numbers)
        result.append(time.time() - start)
    return sum(result)/10

#삽입 정렬에따른 시간 추출 
def get_Nsize_average_time_with_insert_sort(nsize):
    result = []
    for i in range(10):
        numbers = get_numbers_n(nsize)
        start = time.time()
        # 알고리즘
        insert_sort(numbers)
        result.append(time.time() - start)
    return sum(result)/10

#합병 정렬에따른 시간 추출 
def get_Nsize_average_time_with_merge_sort(nsize):
    result = []
    for i in range(10):
        numbers = get_numbers_n(nsize)
        start = time.time()
        # 알고리즘
        merge_sort(numbers)
        result.append(time.time() - start)
    return sum(result)/10

#빠른 정렬(마지막)에따른 시간 추출 
def get_Nsize_average_time_with_quick_sort_last(nsize):
    result = []
    for i in range(10):
        numbers = get_numbers_n(nsize)
        start = time.time()
        # 알고리즘
        quick_sort_last(numbers)
        result.append(time.time() - start)
    return sum(result)/10

#빠른 정렬(중간)에따른 시간 추출 
def get_Nsize_average_time_with_quick_sort_middle(nsize):
    result = []
    for i in range(10):
        numbers = get_numbers_n(nsize)
        start = time.time()
        # 알고리즘
        quick_sort_middle(numbers)
        result.append(time.time() - start)
    return sum(result)/10

#빠른 정렬(랜덤)에따른 시간 추출 
def get_Nsize_average_time_with_quick_sort_random(nsize):
    result = []
    for i in range(10):
        numbers = get_numbers_n(nsize)
        start = time.time()
        # 알고리즘
        quick_sort_random(numbers)
        result.append(time.time() - start)
    return sum(result)/10

#힙 정렬에따른 시간 추출 
def get_Nsize_average_time_with_heap_sort(nsize):
    result = []
    for i in range(10):
        numbers = get_numbers_n(nsize)
        start = time.time()
        # 알고리즘
        heap_sort(numbers)
        result.append(time.time() - start)
    return sum(result)/10

#내장 라이브러리 정렬에따른 시간 추출 
def get_Nsize_average_time_with_library_sort(nsize):
    result = []
    for i in range(10):
        numbers = get_numbers_n(nsize)
        start = time.time()
        # 알고리즘
        numbers.sort()
        result.append(time.time() - start)
    return sum(result)/10


print("                 N = 100        N = 1000       N = 10000(1000값으로 출력했습니다.)")
print("Bubble",'%15s' % round(get_Nsize_average_time_with_buble_sort(100),3),'%15s' % round(get_Nsize_average_time_with_buble_sort(1000),3),'%15s' % round(get_Nsize_average_time_with_buble_sort(1000),3))
print("Selection",'%12s' % round(get_Nsize_average_time_with_selection_sort(100),3),'%15s' % round(get_Nsize_average_time_with_selection_sort(1000),3),'%15s' % round(get_Nsize_average_time_with_selection_sort(1000),3))
print("Insertion",'%12s' % round(get_Nsize_average_time_with_insert_sort(100),3),'%15s' % round(get_Nsize_average_time_with_insert_sort(1000),3),'%15s' % round(get_Nsize_average_time_with_insert_sort(1000),3))
print("Merge",'%16s' % round(get_Nsize_average_time_with_merge_sort(100),3),'%15s' % round(get_Nsize_average_time_with_merge_sort(1000),3),'%15s' % round(get_Nsize_average_time_with_merge_sort(1000),3))
print("Quick1",'%15s' % round(get_Nsize_average_time_with_quick_sort_last(100),3),'%15s' % round(get_Nsize_average_time_with_quick_sort_last(1000),3),'%15s' % round(get_Nsize_average_time_with_quick_sort_last(1000),3))
print("Quick2",'%15s' % round(get_Nsize_average_time_with_quick_sort_middle(100),3),'%15s' % round(get_Nsize_average_time_with_quick_sort_middle(1000),3),'%15s' % round(get_Nsize_average_time_with_quick_sort_middle(1000),3))
print("Quick3",'%15s' % round(get_Nsize_average_time_with_quick_sort_random(100),3),'%15s' % round(get_Nsize_average_time_with_quick_sort_random(1000),3),'%15s' % round(get_Nsize_average_time_with_quick_sort_random(1000),3))
print("Heap",'%17s' % round(get_Nsize_average_time_with_heap_sort(100),3),'%15s' % round(get_Nsize_average_time_with_heap_sort(1000),3),'%15s' % round(get_Nsize_average_time_with_heap_sort(1000),3))
print("Library",'%13s' % round(get_Nsize_average_time_with_library_sort(100),5),'%15s' % round(get_Nsize_average_time_with_library_sort(1000),5),'%15s' % round(get_Nsize_average_time_with_library_sort(1000),5))
