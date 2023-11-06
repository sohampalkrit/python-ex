"""
number of uppercase, lowercase, numerical digits,and other characters in a string.
"""


def string_composition(input_string):
    if type(input_string)==str:
         n=len(input_string)
         c=0
         d=0
         l=0
         e=0
         for i in input_string:
             if i.isupper()==True:
                c+=1
            
             if i.islower()==True:
                 d+=1
             if i.isdigit()==True:
                 l+=1
         e=n-(c+d+l)
         l1=[c,d,l,e]
         return l1
    else:
        raise ValueError("Invalid input. Expecting a string")
    
