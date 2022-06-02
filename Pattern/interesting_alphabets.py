n=int(input("enter n:"))
i=n+1
while(i>=1):
    j=i
    while(j<=n+1):
        x=chr(ord('A')+j-1)
        print(x,end="")
        j+=1
    print("\n")
    i-=1