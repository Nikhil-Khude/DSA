n= int(input("enter no of rows:"))
for i in range (n):
    for j in range(i+1):
        print(chr(65+i),end=" ")
        n+=1
    print()