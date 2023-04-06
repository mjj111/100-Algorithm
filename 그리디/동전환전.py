input_money = int(input("투입할 돈 : "))
weight_of_items = int(input("물건가격 : "))
balance = input_money - weight_of_items
print("거스름돈 : ",balance)
category_of_money = [500,100]
result = []
for change  in category_of_money:
    if(balance // change>0):
        result.append((change,balance // change))
        balance %= change

while(result):
    tmp = result.pop(0)
    change, change_number = tmp[0],tmp[1]
    print(change,"원 동전의 개수 : ",change_number)