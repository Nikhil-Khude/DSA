class node:
    def __init__(self,data,next=None):
        self.next=None
        self.data=data
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
        while(t1.next!=None):
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

    def mid(self,value,x):
        t1=self.head
        while t1.next!=None:
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
        if self.head==None:
            print("link list is empty")
            return
        t1=self.head
        while(t1.next != None):
            if t1.data==value:
                self.head=t1.next
                self.head.prev=None
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

    def print1(self):
        t1=self.head
        while(t1.next != None):
            print(t1.data,end="<-->")
            t1=t1.next
        print(t1.data,end="<-->")

obj=dll()
obj.append(10)
obj.append(20)
obj.append(30)
obj.append(40)
obj.beg(5)
obj.mid(50,30)
obj.delt(20)
obj.print1()