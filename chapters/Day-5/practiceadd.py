class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class sll:
    def __init__(self,head=None):
        self.head=head

    def append(self,value):
        temp=node(value)
        if (self.head!=None):
            t1=self.head
            while(t1.next!=None):
                t1=t1.next
            t1.next=temp
        else:
            self.head=temp

    def beg(self,value):
        temp=node(value)
        temp.next=self.head
        self.head=temp

    def mid(self,value,x):
        temp=node(value)
        t1=self.head

        while(t1.next!=None):
            if(t1.data==x):
                temp.next=t1.next
                t1.next=temp
            t1=t1.next



    def print1(self):
        t1=self.head
        while(t1.next!=None):
            print(t1.data)
            t1=t1.next
        print(t1.data)

obj=sll()
obj.append(10)

obj.append(150)

obj.append(108)

obj.append(104)
obj.beg(50)
obj.mid(600,108)
obj.print1()




