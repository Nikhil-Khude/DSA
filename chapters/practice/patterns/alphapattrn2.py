n= int(input("enter the no rows:"))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()