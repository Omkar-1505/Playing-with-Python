#Time Complexity O(logn) [Height of tree(log n)]
class Node:
    def __init__(self,value):
        self.left =None
        self.right = None
        self.data = value

#For BST the inorder transversal is the same eith the print from smallest to largest and check whether the input is valid or not
def insert(root,value):
    if (root == None):
        return Node(value)
    if (root.data == value):
        return root
    if (root.data > value):
        root.left=insert(root.left,value) #connection with creation
    else:
        root.right=insert(root.right,value)
    return root #if nothing works

def inorder(root):
    if (root != None):
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def search(root,value):
    if (root == None):
        print("Element Not Found")
        return
    if (root.data == value):
        print("Element Found")
        return
    if (root.data > value):
        search(root.left,value)
    else:
        search(root.right,value)

def successor(root): #this is inorder successor we can go for predecessor also
    root=root.right
    while(root!=None and root.left!=None):
        root = root.left
    return root #current location

def delete(root,value):
    if (root==None):
        return root
    if(root.data>value):
        root.left=delete(root.left,value)
    elif(root.data<value):
        root.right=delete(root.right,value)

    else:#got the value
        if(root.left == None):
            return root.right
        if(root.right == None):
            return root.left
#inorder successor = one step right then all left vice-versa for inorder predecessor
#you must have the parent address
#this inorder successor helps to convert the difficulty from deleting 2 childs to 1 or none        
        else:
            suc = successor(root)
            root.data = suc.data
            root.right=delete(root.right,suc.data)
    return root


root = Node(20)
root.left = Node(15)
root.right = Node(30)
inorder(root)
print("\n")
#root = insert(None,val) only used when in beginning if no tree exists
root = insert(root,35)
root = insert(root,56)
root = insert(root,45)
root = insert(root,21)
root = insert(root,11)
inorder(root)
print("\n")
search(root,56)
search(root,100)
print("\n")
delete(root,56)
inorder(root)
print("\n")
delete(root,35)
inorder(root)
print("\n")
delete(root,11)
inorder(root)

#for whole tree it is always O(nlogn)