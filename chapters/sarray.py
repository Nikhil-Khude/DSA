arry =[10,34,45,6,8,20,25,]

min=arry[0]
max=arry[0]

for num in arry:
    if num<min:
        snum=num
        min=num
    if num>max:
        snum=num
        max=num
print("minimum :",min)
print("maximum :",max)