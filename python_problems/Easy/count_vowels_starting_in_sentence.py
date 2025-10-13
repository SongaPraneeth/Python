a= input("enter a sentence: ").split()

count = 0

for i in a:
  if i[0].lower() in 'aeiou':
    count += 1

print(count)


