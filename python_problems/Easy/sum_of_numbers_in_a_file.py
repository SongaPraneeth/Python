import string

# Reads the file
with open(input("enter file name: "), "r") as f:
  re = f.read()

  # Replaces all punctuation with spaces
  for p in string.punctuation:
    re = re.replace(p, ' ')

  # Replaces all letters with spaces
  for p in string.ascii_letters:
    re = re.replace(p, ' ')
  
  # converts them to integers and sums them
  numbers = []
  for i in re.split():
    numbers.append(int(i))

  total = sum(numbers)
  print(total)

  

