def sieve(limit):
    l1=[]
    j=0
    a=0
    while j<=limit:
        def primenumber(num):
          i=1
          c=0
          while i<=num:
              if num%i==0:
                 c+=1
          if c==2:
                return True
          else:
                return False
        if primenumber(j)==True:
            l2=l1.append(j)
        j+=1
    return l2
print("khuh,")
            


