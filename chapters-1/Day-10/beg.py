class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None
        self.prev=None

class dll:
    def __init__(self,head=None):
            self.head=head    

    def append(self,value):
        temp=node(value)
        if self.head==None:
             self.head=temp
             return
        t1=self.head
        while(t1.next !=None):
            t1=t1.next
        t1.next=temp
        temp.prev=t1

    def beg(self,value):
        temp=node(value)
        if self.head==None:
            self.head=temp
            return
        temp.next=self.head
        self.head.prev=temp
        self.head=temp
        

    def print1(self):
        t1=self.head
        while(t1.next!=None):
            print(t1.data,end="<--> ")
            t1=t1.next
        print(t1.data,end=" <-->")

obj=dll()
obj.append(10)
obj.append(20)
obj.append(30)
obj.append(50)
obj.append(40)
obj.beg(5)
obj.print1()
            
