class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class cqueue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
        self.rear.next=self.front #added for circular
    def dequeue(self):
        if self.front:
            temp=self.front
        
            
            if self.front==self.rear:#updated for circular
                self.front=self.rear=None
                print("queue is empty")
            else:
                self.front=self.front.next
            
                self.rear.next=self.front #added for cQueue
            temp=None
            
        else:
            print("queue is empty")

    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end="->")
            temp=temp.next
            if temp==self.front:
                break
        print()
qu=cqueue()
qu.enqueue(node(10))
qu.enqueue(node(20))
qu.enqueue(node(30))
qu.enqueue(node(40))
qu.print()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.print()
qu.enqueue(node(60))
qu.enqueue(node(50))
qu.print()