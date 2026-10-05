from array import *
val=array('i',[])
n= int(input("enetr the no you want in array:"))
for i in range(n):
    m=int(input("enetr the next no:"))
    val.append(m)

for x in val:
    print(x , end=" ")                
