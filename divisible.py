#Python Program to Print all Numbers in a Range Divisible by a Given Number
n=int(input("Enter the upper num"))
m=int(input("Enter the lower num"))
n=int(input("Enter divisible num"))
for i in range(n,m):
    if(i%n==0):
        print(i)