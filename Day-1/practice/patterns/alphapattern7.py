n=int(input("enter the no of rows:"))
p=int(input("enter the no of chr:"))
for i in range (n):
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=2
    print()