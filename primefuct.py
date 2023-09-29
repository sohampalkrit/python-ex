x=int(input("enter a number="))
i=1
c=0
while i<=x:
        if x%i==0:
            c+=1
        i+=1
if c==2:
        print("This is a prime number")
else:
        print("Not a prime number")
    
