n=int(input("enter a number: "))
esum=0
osum=0
while(n>0):
    d=n%10
    if(d%2==0):
        esum=esum+d
    elif(d%2!=0):
        osum=osum+d
    n=n//10
print("even sum = ",esum)
print("odd sum = ",osum)