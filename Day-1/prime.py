num =int(input("enter your no : "))
flag=0
for i in range(2,(num//2)+1):
    if (num % 1 ==0):
        flag=1
        break
    if (flag==1):
                print("not prime")

    else:
        print("prime")
