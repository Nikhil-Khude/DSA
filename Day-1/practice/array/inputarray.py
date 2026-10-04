from array import *
val=array('i',[])
n= int(input("Enter the number of elements you want to add in the array:"))
for i in range(0,n):
    m=int(input("enetr th enxt no.:"))
    val.append(m)

for n in val:
    print(n)


from array import *
val=array('i',[])
n= int(input("enetr the no you want in array:"))
for i in range(n):
    m=int(input("enetr the next no:"))
    val.append(m)

for x in val:
    print(x , end=" ")                
