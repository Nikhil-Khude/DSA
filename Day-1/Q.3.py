arr = [1,10,12,30,45,63,52,32,52]

min=arr[0]
max=arr[0]

for num in arr:
    if num<min:
             min=num
    if num>max:
             max=num
print("manimum :",min)
print("maximum :",max)


