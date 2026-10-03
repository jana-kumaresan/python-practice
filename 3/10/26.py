try :
  age =-5
  if age < 0 :
    raise ValueError ("age cannot be negative")
  print("age:",age)  
except ValueError as e:
  print("error :",e)


