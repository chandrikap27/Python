n=int(input("enter the size of n : "))
for i in range(1,n+1):
    c=1
    for j in range(n,0,-1):
        if j >i :
            print(" ",end='')
        else:
            print(c,end='')
            c+=1
    print(" ")