#Hierarchial Data Structure
#Non-linear -> Tree, Graph
#for array representation of tree only works on complete binary tree; {(index of value)*2 +1}=Left child and {(index of value)*2 +2}=Right child

#Tree traversal
#Pre-order goes by recursion
class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value

def preorder(root): #as it is written outside the class then we don't need to call self repeatedly when called
    if (root != None):
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
        

def postorder(root):
    if (root != None):
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def inorder(root):
    if (root != None):
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
        

root = Node(1)
root.left = Node(2)
root.right=Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
preorder(root)
print("\n")
inorder(root)
print("\n")
postorder(root)