class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def buildtree(inorder,preorder,inStrt,inEnd):
    if(inStrt > inEnd):
        return None

    temp=Node(preorder[buildtree.preIndex])
    buildtree.preIndex+=1

    #If this node has no children then return temp
    if inStrt==inEnd:
        return temp

    #Else find the index of this node in Inorder Traversal
    inIndex=search(inorder,inStrt,inEnd,temp.data)

    #Using Index in Inorder Traversal construct left and right subtrees
    temp.left=buildtree(inorder,preorder,inStrt,inIndex-1)
    temp.right=buildtree(inorder,preorder,inIndex+1,inEnd)
    return temp

#UTILITY FUNCTION
#Search - Function to find index of value in arr[start....end]
#printInorder - The function assumes that value is present in inorder[]

def search(arr,start,end,value):
    for i in range(start,end+1,1):
        if(arr[i]==value):
            return(i)

def printInorder(node):
    if node is None:
        return

    #First recursion on left child
    printInorder(node.left)
    printInorder(node.data)
    printInorder(node.right)

inorder=[1,2,4,8,9,10,11,5,3,6,7]
preorder=[8,4,10,9,11,2,5,1,6,3,7]
buildtree.preIndex=0
root=buildtree(inorder,preorder,0,len(inorder)-1)
print("Inorder :")
printInorder(root)