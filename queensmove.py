def queensmove(a,b,c,d):
    l1=[(a,j)for j in range(1,9)]
    l2=[(i,b)for i in range(1,9)]
    l3=[(a+i,b+i)for i in range(1,9-a)]
    l4=[(a-i,b-i) for i in range(1,a)]
    l5=[[(a-j,b+i) for i in range(1,9-b) for j in range(1,a) ][a-2]]
    l6=[[(a+i,b-j) for i in range(1,9-a) for j in range(1,b)][b-2]]
    ltot=l1+l2+l3+l4+l5+l6
    l7=[(c,j)for j in range(1,9)]
    l8=[(i,d)for i in range(1,9)]
    l9=[(c+i,d+i)for i in range(1,9-c)]
    l10=[(c-i,d-i) for i in range(1,c)]
    if c!=1:
        l11=[[(c-j,d+i) for i in range(1,9-d) for j in range(1,c) ][c-2]]
    else:
        l11=[]
    if d!=1:
         l12=[[(c+i,d-j) for i in range(1,9-c) for j in range(1,d)][d-2]]
    else:
        l12=[]
    ltot2=l7+l8+l9+l10+l11+l12

    l=[(i,j) for i in ltot for j in ltot2 if i==j]
    if len(l)>0:
        return True
    else:
        return False
    
print(queensmove(2,2,1,1))

