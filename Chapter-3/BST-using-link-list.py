class node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

class bst:
    def __init__(self):
        self.root=None
    def insert(self,new_node):
        if self.root is None: #BST is empty
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right

    def inorder(self,rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)

b1=bst()
b1.insert(node(100))
b1.insert(node(10))
b1.insert(node(450))
b1.insert(node(0))
b1.insert(node(65))
b1.insert(node(300))
b1.inorder(b1.root)