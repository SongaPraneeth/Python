l = [5,7,3,0,1,9,4,6,10,2,8,22]

largest = l[0]
smallest = l[0]
for i in range(1,len(l)):
  if largest > l[i]:
    largest = largest
  else:
    largest = l[i]

  if smallest < l[i]:
    smallest = smallest
  else:
    smallest = l[i]

print("Largest number is: ",largest)
print("smallest number is: ",smallest)