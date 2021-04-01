class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,value):
        p=Node(value)
        p.next=self.head
        self.head=p

    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def detectloop(self):
        slow_p=self.head
        fast_p=self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p=slow_p.next
            fast_p=fast_p.next.next
            if(slow_p==fast_p):
                return
node=LinkedList()
node.push(20)
node.push(4)
node.push(15)
node.push(10)
if(node.detectloop()):
    print("found loop\n")
else:
    print("no loop\n")