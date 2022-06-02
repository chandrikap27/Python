print("1.sum")
print("2.diff")
print("3.product")
print("4.quotient")
print("5.remainder")
i = int(input("Enter the choice : "))
res=0
if(i==1):
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2st number: "))
    res=a+b
    print("result = ",res)
elif(i==2):
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2st number: "))
    res=a-b
    print("result = ",res)
elif(i==3):
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2st number: "))
    res=a*b
    print("result = ",res)
elif(i==4):
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2st number: "))
    res=a/b