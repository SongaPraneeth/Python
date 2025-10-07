#manually printing puntuations

e = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
l = []
i = 33
while i < 64 :
  if i in e:
    i += 1
    continue
  else:
    a = chr(i)
    l.append(a)
  
  i += 1
print(l)



z = input("Enter a string : ").strip()

str_i = ""

for i in z:
  if i not in l:
    str_i += i
    

print(str_i)
