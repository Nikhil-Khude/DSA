n=int(input("enter the no of rows:"))
p=int(input("enter the no of chr:"))
for i in range (n):
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(i,n-1):
        print(chr(p),end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
    p-=1
    print()