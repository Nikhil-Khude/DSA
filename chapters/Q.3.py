arr = [10,5,4,1,20,53,56,54,21,36]
min=arr[0]
max=arr[0]

for num in arr:
    if num<min:
        min=num

    if num>max:
        max=num
print("minimum :",min)
print("maximum :",max)