def steps(number):
  if number>0:
    l1=[]
    while number!=1:
        if number%2==0:
            number=number//2
        else:
            number=3*number+1
        l1.append(number)
    return len(l1)
  else:
     raise ValueError("Invalid input.")
print(steps(77777))