n = int(input("Enter a number to find how many prime number are present under that number: "))
i = 2

while i <= n:
  z = 2
  count = 0

  while z < i:
    if i % z == 0 :
      count = count + 1
    z +=1 
    
  if count == 0 :
    print(i)
  i += 1
