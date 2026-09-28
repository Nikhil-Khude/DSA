arr = [10,34,45,6,8,20,25,10]
min=arr[0]
max=arr[0]
for num in arr:
        if num<min:
                min=num
        if num>max:
                max=num
print("minimum:",min)
print("maximum",max)