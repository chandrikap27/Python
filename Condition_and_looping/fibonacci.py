n=int(input("enter n(position):"))
a = 0
b = 1
if n == 0:
    print(a)
if n == 1:
    print(b)
if n >= 2:
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    print(b)