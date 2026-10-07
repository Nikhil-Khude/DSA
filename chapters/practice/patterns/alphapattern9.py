n=int(input("enter the no of rows:"))
for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print('A',end=" ")
        else:
            print('B',end=" ")
    print()
