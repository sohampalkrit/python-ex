#arabic to roman till 1000s
def arabictoroman(num):
    k=len(str(num))
    
    
    if 1>0:
       l1=list(str(num))
       def singledigit(n,place):
          if place==1:
              if n==0:
                 l2=''
              l2=['I' for i in range(n) if 0<n<4]
              if n==4:
                  return ['IV']
              if n==9:
                  return ['IX']

              if n>4:
                  l2=['V']+['I' for i in range(1,n-4)]
              #return l2
          if place==2:
              n=int(l1[len(l1)-2])
              l2=['X' for i in range(n) if n<4]+singledigit(int(l1[len(l1)-1]),1)
              if n==4:
                  return ['XL']+singledigit(int(l1[len(l1)-1]),1)
              if n==9:
                  return ['XC']+singledigit(int(l1[1]),1)
              if n>4:
                  l2=['L']+['X' for i in range(1,n-4)]+singledigit(int(l1[len(l1)-1]),1)
              #return l2
          
          if place==3:
              n=int(l1[0])
              l2=['M' for i in range(n) if n<4]+singledigit(int(l1[len(l1)-2]),2)
              if n==4:
                  return ['CD']+singledigit(l1[len(l1-2)],2)
              if n==9:
                  return ['CM']+singledigit(l1[len(l1)-1],2)
              if n>4:
                  l2=['D']+['C' for i in range(1,n-4)]+singledigit(int(l1[len(l1)-2]),2)
              #return l2 

          #return l2[0]
    if num==1000:
        return 'M' 
    res=''    
    for i in singledigit(num,k):
        res=res+i
    return res
print(arabictoroman(999)) 








