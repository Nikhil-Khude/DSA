class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class queue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def dequeue(self):
        if self.front:
            temp=self.front
            self.front=self.front.next
            if self.front==None:
                self.rear=None
                print("queue is empty")
            temp=None
        else:
            print("queue is empty")

    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print()
qu=queue()
qu.enqueue(node(10))
qu.enqueue(node(20))
qu.enqueue(node(30))
qu.enqueue(node(40))
qu.print()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.enqueue(node(60))
qu.enqueue(node(50))
qu.print()