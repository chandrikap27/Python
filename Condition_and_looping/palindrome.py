n=input("enter a number:")
n=int(n)
m=int(0)
n1=int(n)
#m=0
while n>0:
    r=int(n%10)
    m=m*10+r
    n=int(n/10)
if(n1==m):
    print("true")
else:
    print("false")