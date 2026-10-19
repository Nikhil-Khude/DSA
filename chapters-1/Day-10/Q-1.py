class node:
    def __init__(self,info,next=None):
        self.data=info
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
    def beg(self,value):
        temp=node(value)
        t1=self.head
        

    
        
    def print1(self):
        t1=self.head
        while(t1.next !=None):
            print(t1.data, end=" ")
            t1=t1.next
        print(t1.data, end=" ")

obj=sll()
obj.append(10)
obj.append(20)
obj.append(30)
obj.print1()

        