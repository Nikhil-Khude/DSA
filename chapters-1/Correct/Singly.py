class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class sll:
    def __init__(self,head=None):
        self.head=head

    def append(self,value):
        temp=node(value)
        if self.head != None:
            t1=self.head
            while(t1.next != None):
                t1=t1.next
            t1.next=temp
            
        else:
            self.head=temp

    def mid(self,value,x):
        temp=node(value)
        t1=self.head
        while(t1.next!=None):
            if t1.data ==x:
                temp.next=t1.next
                t1.next=temp
                break
            else:
                t1=t1.next
        
            
    def beg(self,value):
            temp=node(value)
            temp.next=self.head
            self.head=temp

    def delt(self,value):
        t1=self.head
        prev=t1
        if t1.data==value:
            self.head=t1.next
            return
        while(t1.next != None):
            if t1.data==value:
                prev.next=t1.next
                return
            else:
                prev=t1
                t1 = t1.next
                
        if (t1.data==value):
            prev.next=None

            
    def print1(self):
        t1=self.head
        while(t1.next != None):
            print(t1.data,end=" ")
            t1=t1.next
        print(t1.data,end=" ")
obj=sll()
obj.append(10)
obj.append(20)
obj.append(30)
obj.beg(5)
obj.mid(40,20)
obj.delt(20)
obj.print1()