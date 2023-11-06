def sieve(limit):
    l1=[]
    j=0
    a=0
    while j<=limit:
        k=0
        while k<=limit:
          i=1
          c=0
          while i<=k:
              if k%i==0:
                 c+=1
              i+=1
          k+=1
              
          if c==2:
                l2=l1.append
            
        j+=1
    return l2
print(sieve(10))

