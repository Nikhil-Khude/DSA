class node:
    def __init__(self,value,next=None):
        self.data=value
        self.next=next
        self.prev=None

class dll:
    def __init__(self,head=None):
        self.head=head

    def append(self,value):
        temp=node(value)
        if self.head ==None:
            self.head=temp
            return
        t=self.head
        while t.next !=None:
            t=t.next
        
        t.next=temp
        temp.prev=t

    def print1(self):
        t=self.head
        while t.next!=None:
            print(t.data, end="<-->")
            t=t.next
        print(t.data, end="<-->")

obj=dll()
obj.append(10)
obj.append(20)
obj.append(30)
obj.print1()

        

        