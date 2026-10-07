n=int(input("enter the number of rows:"))
for i in range(n):
    p=65
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
        p+=1
    print()