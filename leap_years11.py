def is_leap_year(y):
  if y>=0:
    if y%100!=0 or y%400==0:
        if y%4==0:
            return True
        else:
            return False
    else:
        return False
  else:
     raise ValueError("input should not be negative")
