#Python Program to Find the Smallest Among Three Numbers
a=input("Enter a number :")
b=input("Enter a number :")
c=input("Enter a number :")

if(a<b) and (a<c):
    print("A is smaller:",a)
elif(b<a) and (b<c):
    print("B is smaller:",b)
elif(c<a) and (c<b):
    print("c is smaller:",c)