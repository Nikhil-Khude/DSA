class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
        self.prev=None
class dll:

    def __init__(self,head=None):
        self.head=None

    def append(self,value):
        temp=node(value)
        if self.head != None:
            t1=self.head
            while t1.next != None:
                t1=t1.next
            t1.next=temp
            temp.prev=t1
        else:
            self.head=temp

    def beg(self,value):
        temp=node(value)
        if self.head != None:
            t1=self.head
            temp.next=self.head
            self.head=temp
        else:
            self.head=temp

    def mid(self,value,x):
        t1=self.head
        while t1.next !=None:
            if t1.data==x:
                break
            else:
                t1=t1.next

        temp=node(value)
        temp.next=t1.next
        t1.next.prev=temp
        t1.next=temp
        temp.prev=t1
    def delt(self,value):
        t1=self.head
        if t1.data==value:
            self.head=t1.next
            return
        while t1.next != None:
            if t1.data==value:
                t1.prev.next=t1.next
                t1.next.prev=t1.prev
                return
            else:
                t1=t1.next
        if t1.data==value:
            t1.prev.next=None

    def print(self):  
        t1=self.head
        while t1.next !=None:
            print(t1.data)
            t1=t1.next
        print(t1.data)

obj=dll()
obj.append(10)      
obj.append(20)      
obj.append(30)      
obj.append(40)  
obj.beg(5)   
obj.mid(50,20)   
obj.delt(50)
obj.print()    