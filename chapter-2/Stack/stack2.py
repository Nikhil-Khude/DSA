class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp=self.top
            print("poped element")
            self.top=self.top.next
            temp=None

    def print(self):
        temp=self.top
        print("stack elementt")
        while temp:
            print(temp.data)
            temp=temp.next

st=stack()
st.push(node(100))
st.push(node(200))
st.push(node(300))
st.push(node(400))
st.print()
        
        