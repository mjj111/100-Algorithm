import sys
import csv
import datetime


def sort_csv_ip():
    csv_file.sort(key = lambda x : (x[0],x[1]))
    print_csv()
    return 


def sort_csv_time():
    csv_file.sort(key = lambda x : x[1])
    print_csv()
    return 


def print_csv():
    for i in range(len(csv_file)):
        print(csv_file[i][1])
        print('    IP','.'.join(csv_file[i][0]))
        print('    URL',csv_file[i][2])
        print('    Status',csv_file[i][3])
    return

def csv_file_formatting():
    csv_file_datetime_formatting()
    csv_file_ip_formatting()
    return 

def csv_file_datetime_formatting():
    for i in range(len(csv_file)):
        csv_file[i][1] = datetime.datetime.strptime(str(csv_file[i][1][1:]),'%d/%b/%Y:%H:%M:%S')
    return


def csv_file_ip_formatting():
    for i in range(len(csv_file)):
        csv_file[i][0] = list(csv_file[i][0].split('.'))
    return 


def read_csv(arg):
    to_sort_file = ''
    file_path = f"/Users/82105/desktop/{arg}"
    f = open(file_path, "r", encoding="utf-8")
    to_sort_file = csv.reader(f)
    for line in to_sort_file:
        csv_file.append(list(line))
    csv_file.pop(0)
    
    csv_file_formatting()
    
    return



def process_command():
    command = input()
    return command[:-1]


csv_file = []
while True:
    command= input()
    if command == "exit":
        break

    elif command == "print":
        print_csv()
    
    else:
        command,arg = command.split()
        if command == 'read' :
            read_csv(arg)
        
        elif command == "sort" and arg == '-t':
            sort_csv_time()
            
        elif command == "sort" and arg == '-ip':
            sort_csv_ip()
