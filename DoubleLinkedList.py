class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.start=None

    def CreateList(self):
        y=1
        if(self.start==None):
            temp=self.start
            value=int(input("Enter first data\n"))
            p=node(value)
            p.prev=None
            p.next=None
            p.prev=temp
            self.start=p
            temp=self.start
        while(y==1):
            value=int(input("Enter second node data\n"))
            p=node(value)
            p.next=None
            p.prev=None
            temp.next=p
            p.prev=temp
            temp=p
            y-=1
            y=int(input(" Want insertion 1 or 0 \n"))

    def InsAtBeg(self):
        if(self.start==None):
            print("Linked List is empty")
        else:
            value=int(input("Enter node data for beginning\n"))
            p=node(value)
            p.prev=None
            p.next=self.start
            self.start.prev=p
            self.start=p

    def InsAtMid(self):
        temp=self.start
        pos=int(input("Enter the insertion position\n"))
        value = int(input("ENter node data for insertion at middle\n"))
        p=node(value)
        p.prev = None
        p.next = None
        i=0
        while(temp!=None):
            if(i==pos-1):
                p.prev=temp
                p.next=temp.next
                if(temp.next==None):
                    temp.next.prev=p
                temp.next=p
            temp=temp.next
            i+=1

    def DelAtBeg(self):
        temp=self.start
        self.start=temp.next

    def DelAtMid(self):
        temp=self.start
        pos=int(input("Enter position for mid deletion\n"))
        for i in range(pos-1):
            temp=temp.next
        k=temp.next.next
        temp.next.prev = None
        temp.next=None
        temp.next=k

    def traversing(self):
        temp=self.start
        while(temp!=None):
            print(temp.data,end=" ")
            temp=temp.next
        print()

object=DoubleLinkedList()
object.CreateList()
object.InsAtBeg()
object.InsAtMid()
object.DelAtBeg()
object.DelAtMid()
object.traversing()