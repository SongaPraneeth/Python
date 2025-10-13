a = [1,3,42,4,5,10,4]
b = [9,77,44,33,5,0,5,5]

c = []

for i in a:
  if i in b:
    c.append(i)

print(c)