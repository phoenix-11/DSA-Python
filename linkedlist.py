class node:
    def __init__(self,data):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.start=None

    def CreateL(self):
        y=1
        if(self.start==None):
            value = int(input("Enter data1\n"))
            p = node(value)
            p.next = None
            self.start = p
            temp = self.start
        while(y==1):
            value=int(input("Enter data2\n"))
            p=node(value)
            p.next=None
            temp.next=p
            temp=p
            y=y-1
            y=int(input("1 or 0"))

    def InsAtMed(self):
        temp=self.start
        pos=int(input("Enter position for middle insertion\n"))
        value=int(input("Enter node data\n"))
        p=node(value)
        p.next=None
        i=0
        while(temp!=None):
            if(i==pos):
                p.next=temp.next
                temp.next=p
            i+=1
            temp=temp.next

    def InsAtEnd(self):
        temp=self.start
        value=int(input("Enter node data for end\n"))
        p=node(value)
        while(temp.next!=None):
            temp=temp.next
        temp.next=p
        p.next=None

    def traversing(self):
        temp=self.start
        if(temp.next==None):
            print("Linked List is empty\n")
        else:
            print("linked List : ")
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
            print()

    def DelAtBeg(self):
        if(self.start==None):
            print("Linked List is empty\n")
        else:
            temp=self.start
            self.start=temp.next

    def DelAtMid(self):
        if(self.start==None):
            print("Linked List is empty\n")
        else:
            pos=int(input("Enter position for deletion of node\n"))
            i=0
            temp=self.start
            for i in range(pos-1):
                temp=temp.next
            k=temp.next.next
            temp.next=None
            temp.next=k

    def sorting(self):
        if(self.start==None):
            print("Linked List is empty\n")
        else:
            print("Here is your sorted Linked List : ")
            temp=self.start
            while(temp!=None):
                p=temp.next
                while(p!=None):
                    if(temp.data>p.data):
                        swap=temp.data
                        temp.data=p.data
                        p.data=swap
                    p=p.next
                temp=temp.next

    def reverse(self):
        prev=None
        temp=self.start
        while(temp!=None):
            swap=temp.next
            temp.next=prev
            prev=temp
            temp=swap
        self.start=prev

object=LinkedList()
object.CreateL()
object.InsAtMed()
object.InsAtEnd()
object.DelAtBeg()
object.DelAtMid()
object.reverse()
object.traversing()
object.sorting()
object.traversing()