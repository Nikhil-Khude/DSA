class node():
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

def preOrder(root):
    if root != None:
        print(root.data,end=" ")
        preOrder(root.left)
        preOrder(root.right)


def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)

def postOrder(root):
    if root != None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data,end=" ")

root=node(1)
root.left=node(3)
root.right=node(5)
root.left.left=node(2)
root.left.right=node(4)
root.right.right=node(8) 
print("Postorder:-")   
postOrder(root)
print("\npreorder:-")
preOrder(root)
print("\ninorder:-")
inOrder(root)


        