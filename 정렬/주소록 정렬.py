import csv
import pandas as pd
import os
from collections import defaultdict

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        
class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None


    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data[0] <= node.data[0]:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    
    def trace(self, key):
        result =self._trace_value(self.root, key)
        self.print_node_data(result)
        return 
    
    
    def _trace_value(self, root, key):
        if root is None or root.data[0] == key:
            return root.data
        elif key < root.data[0]:
            self.print_node_data(root.data)
            return self._find_value(root.left, key)
        else:
            self.print_node_data(root.data)
            return self._find_value(root.right, key)


    def find(self, key):
        result =self._find_value(self.root, key)
        if not result:
            return False
        self.print_node_data(result)
        return True


    def _find_value(self, root, key):
        if root is None or root.data[0] == key:
            return root.data
        elif key < root.data[0]:
            if not root.left:
                return False 
            return self._find_value(root.left, key)
        elif key >= root.data[0]:
            if not root.right:
                return False 
            return self._find_value(root.right, key)

        
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted


    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data[0]:
            deleted = True
            print("아래는 삭제된 노드입니다. ")
            self.print_node_data(node.data)
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data[0]:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted     
        # 중위순회
    def inorder_traverse(self):
        if self.root is not None:
            self.__inorder(self.root)

    def __inorder(self, node):
        if node.left is not None:
            self.__inorder(node.left)

        self.print_node_data(node.data)
        
        if node.right is not None:
            self.__inorder(node.right)
            
            
    def print_node_data(self,result):
        print(result[0])
        print("\tCompany: ",result[1])
        print("\tAddress: ",result[2])
        print("\tZipcode: ",result[3])
        print("\tPhone: ",result[4])
        print("\tEmail: ",result[5])
        print()
        return  
    
            
            
     # 저장을 위한 중위순회
    def inorder_traverse_to_save(self):
        if self.root is not None:
            self.__inorder_to_save(self.root)

    def __inorder_to_save(self, node):
        if node.left is not None:
            self.__inorder_to_save(node.left)
        global to_save_result 
        to_save_result.append(node.data)
        
        if node.right is not None:
            self.__inorder_to_save(node.right)

            
 
 

def read_tsv(arg):
    to_sort_file = ''
    
    file_path = f"/Users/82105/desktop/{arg}"
    f = open(file_path, "r", encoding="utf-8")
    to_sort_file = csv.reader(f)
    for line in to_sort_file:
        tsv_file.append("".join(list(line)).split("\t"))
    tsv_file.pop(0)
    for line in tsv_file:
        tsv_binary_search_tree.insert(line)  
    return

tsv_binary_search_tree = BinarySearchTree()
tsv_file = []
result = []
to_save_result =[]
while True:
    command= input()
    if command == "exit":
        break
    
    elif command == "list":
        result = []
        tsv_binary_search_tree.inorder_traverse()
        
    elif command == "save":
        to_save_result = []
        tsv_binary_search_tree.inorder_traverse_to_save()
        save_file = pd.DataFrame(to_save_result, columns=['name', 'company', 'address','zip','phone','email'])
        os.chdir('C:/Users/82105/Desktop')
        save_file.to_csv('algorithm_assigment06_result.csv', index=False, encoding='cp949') 
        print("저장완료 되었습니다.") 
        
    else:
        command,arg = command.split('-')
        if command == 'read' :
            read_tsv(arg)
        
        elif command == "find":
            result = tsv_binary_search_tree.find(arg)
            if not result:
                print("없는 회원입니다.")
            
        elif command == "delete":
            tsv_binary_search_tree.delete(arg)
        
        elif command == "add":
            tmp_list = []
            tmp_list.append(arg)
            tmp_list.append(input("Company? "))
            tmp_list.append(input("Address? "))
            tmp_list.append(input("Zip? "))
            tmp_list.append(input("Phone? "))
            tmp_list.append(input("Email? "))
            
            if tsv_binary_search_tree.find(arg):
                print("이미 동일 이름이 존재하여 거부합니다.")
            else: 
                tsv_binary_search_tree.insert(tmp_list) 
                print("추가 완료되었습니다.")
                tsv_binary_search_tree.find(arg)