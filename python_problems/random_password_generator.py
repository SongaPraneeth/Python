import random
import string
fe = int(input("Enter the lenght of the password: "))

z = string.ascii_letters + string.digits + string.punctuation

password =""

for i in range(fe):
  b = random.choice(z)
  password = password+b

print(password)
