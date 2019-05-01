#Python Program to Find the Largest Among Three Numbers
a=input("Enter number")
b=input("Enter number")
c=input("Enter number")

if(a>b) and (a>c):
    print ("A is greater:",a)
elif (b>a) and (b>c):
    print("b is greater:",b)
else:
    print("c is greater:",c)