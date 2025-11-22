import re

def sumofnumbers(n) -> int:

  numbers = re.findall(r"\d+",n)
  print(numbers)
  return sum(map(int,numbers))
    
  
stringwithnumbers = input("Enter the string: ")

print(sumofnumbers(stringwithnumbers))
