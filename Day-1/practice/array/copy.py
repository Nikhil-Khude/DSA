from array import *
val =array('i',[1,2,3,4,5,6])
num=array(val.typecode,(n for n in val))
num.insert(2,10)
for i in range(0,len(num)):
    print(num[i],end="   ")
