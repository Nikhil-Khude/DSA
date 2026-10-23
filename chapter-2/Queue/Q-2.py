class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class queue:
    def __init__(self):
        self.front=None
        self.rare=None

    def enqueue(self,value):
        new_node=node(value)
        if self.rare is None:
            self.front=self.rare=new_node
            return
        else:
            self.rare.next=new_node
            self.rare=new_node

    def dequeue(self):
        if self.rare==None:
            return "queue is empty"
        else:
            temp=self.front
            self.front=temp.next
            if self.front is None:
                self.rare=None
            return(temp.data)


    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print()

qu=queue()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
qu.enqueue(40)
print("queue",end=" ")
qu.print()
print("dequeue is:",qu.dequeue())
print("dequeue is:",qu.dequeue())
print("dequeue is:",qu.dequeue())
print("dequeue is:",qu.dequeue())
print("dequeue is:",qu.dequeue())

