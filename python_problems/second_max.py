a = [14,3,7,9,12,4,13,6,6,8]

b = 0
index_numb = 0
largest = a[0]
for i in range(1,len(a)):
  if largest < a[i]:
    largest = a[i]
    index_numb  = i


if index_numb != 0:
  second_largest = a[0]
else:
  second_largest = a[1]

for i in range(1,len(a)):
  if largest == a[i]:
    continue
  else:
    if second_largest < a[i]:
      second_largest = a[i]

print(second_largest)



# a = [14,3,7,9,12,4,13,6,6,8]

# unique = list(set(a))  # remove duplicates
# unique.sort(reverse=True)
# print(unique[1])  # second largest


