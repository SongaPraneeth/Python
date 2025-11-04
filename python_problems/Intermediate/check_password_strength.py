import string



upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
special_charcters = list(string.punctuation)
digits = ['0','1','2','3','4','5','6','7','8','9']



password = input("Enter the password: ")

a = 0
b = 0
c = 0
d = 0

if len(password) >= 12 : 
  for i in password:
    if i in upper:
      a += 1
    elif i in lower:
      b += 1
    elif i in digits:
      c += 1
    elif i in special_charcters:
      d += 1
      
  if a > 0 and b > 0 and c > 0 and d > 0:
    print("The password is strong")
    
  else: 
    print("The password is not strong")
    
else: 
  print("The password is not strong")