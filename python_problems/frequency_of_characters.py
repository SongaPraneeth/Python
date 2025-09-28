def fre(i: str) -> dict:
  d = {}
  for z in i:
    if z in d:
      d[z] +=1
    else:
      d[z] = 1
  return d

i = input("enter a string: ")
print(fre(i))