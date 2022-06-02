n=int(input("enter n:"))
i=1
for i in range(1,n+1):
    j=1
    for j in range(1,i+1):
        print("*",end="")
        j+=1
    print("\n")
    i+=1