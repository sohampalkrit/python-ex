def primefactors(n):
    l1=[i for i in range(1,n+1) if n%i==0]
    
    def prime(num):
        j=1
        c=0
        while j<=num:
            if num%j==0:
                c+=1
            j+=1
        if c==2:
            return True
        else:
            return False
    l2=[]
    for j in l1:
        if prime(j)==True:
            l2.append(j)
    l3=[]
    for i in l2:
       while n%i==0:
           l3.append(i)
           n=n/i
    return l3 
print(primefactors(12))
