from collections import deque
d = deque()
d.append([1,2])
a ,b = d.popleft()
print(a,b)
#popleft 리스트로 넣고 뽑어도 된다. 