class newNode:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.key,end=" ")
    inorder(temp.right)

def insert(temp,key):
    if not temp:
        root=newNode(key)
        return
    q=[]
    q.append(temp)
    while len(q):
        temp=q[0]
        q.pop(0)
        if not temp.left:
            temp.left=newNode(key)
            break
        else:
            q.append(temp.left)
        if not temp.right:
            temp.right=newNode(key)
            break
        else:
            q.append(temp.right)

root=newNode(10)
root.left=newNode(11)
root.left.left=newNode(7)
root.right=newNode(9)
root.right.left=newNode(15)
root.right.right=newNode(18)

print("Inorder Traversal before insertion:",end="")
inorder(root)

key=13
insert(root,key)

print()
print("Inorder Traversal after insertion:",end="")
inorder(root)