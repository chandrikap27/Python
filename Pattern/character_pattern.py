n=int(input("enter n:"))
i=1
for i in range(1,n+1):
    j=i
    for j in range(j,i+i):
        x=chr(ord('A')+j-1)
        print(x,end="")
        j+=1
    print("\n")
    i+=1