class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=Node
    def Insert(self,data):
        new_node=Node(data)
        if self.head is none:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=next_node
    def display(self):
        current=self.head
        while current:
            print(current.data.ends="->")
            current = current.next
        print("None")

#Usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
