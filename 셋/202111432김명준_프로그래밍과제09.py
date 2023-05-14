words = {}
edge = 0
f = open("C:\\Users\\alstj\\Desktop\\알고리즘\\2023_algorithm\\python\\week9.txt" , "r", encoding="utf-8")

while 1 :
    file = f.readline() 
    if file == '':
        break;
    data = file.split("\t")
    words[data[0]] = [data[1].replace('\n', '')]

for i,j in words.items():
        split_value = j[0].split(" ")
        for z in split_value:
            if z in words and i != z:   
                if z not in j :    
                    words[z].append(i)     
                    words[i].append(z)
                edge += 1       
                
max = 0
maxvalue = ""
for i in words.keys():
    del words[i][0]     
    if max < len(words[i]):
         max = len(words[i])
         maxvalue = i

ans3_count = 0
ans3_visted = []
def answer3(word) :
    if ans3_visted != False:
        return
    ans3_visted.append(word)
    for i in words[word]:
        answer3(i)
for i in words:
    if i not in ans3_visted:
        ans3_count += 1
        answer3(i)

ans4_count = 0
ans4_word = []
def answer4(word,index) :
    for i in words[word]:
        global ans4_word, ans4_count,b
        if i not in ans4_word:
            ans4_word.append(i)
            print(i)
            ans4_count+=1
            if index <= b :
                answer4(i, index+1)

print("Answer 1:", len(words), edge)
print("Answer 2:", maxvalue, max)
print("Answer 3:", ans3_count)
print("Answer 4:")
a = input()
b = int(input())
answer4(a,0)
print(ans4_count)