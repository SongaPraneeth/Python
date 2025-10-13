def gcd(a, b):
  rem = 1
  while rem!= 0:
    rem = a %b
    a = b
    b = rem
  return a 
    

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD is:", gcd(num1, num2))




