'''
def sum_digits(n):
  z = 0
  while n > 0:
    a = n%10
    z = z + a
    n = n//10
  return z 
  
num = int(input("Enter a number:"))

print(sum_digits(num))
'''

def sum_digits(n: int) -> int:
    return sum(int(d) for d in str(n))

num = int(input("Enter a number:"))

print(sum_digits(num))