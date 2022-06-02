#Rectangular Area
#You are given a rectangle in a plane. The corner coordinates of this rectangle is provided to you. You have to print the amount of area of the plane covered by this rectangles.
#The end coordinates are provided as four integral values: x1, y1, x2, y2. It is given that x1 < x2 and y1 < y2.
#Input format:
#The first line of input contains an integer x1 (1 <= x1 <= 10)
#The second line of input contains an integer y1 (1 <= y1 <= 10) 
#The third line of input contains an integer x2 (1 <= x2 <= 10)
#The fourth line of input contains an integer y2 (1 <= y2 <= 10) 
#Output format:
#The first and only line of output contains the result.  
#Sample Input:
#1
#1
#3
#3
#Sample Output:
#4

x1=input("enter x1:")
x1=int(x1)
y1=input("enter y1:")
y1=int(y1)
x2=input("enter x2:")
x2=int(x2)
y2=input("enter y2:")
y2=int(y2)
l=int(x2-x1)
b=int(y2-y1)
print(l*b)

