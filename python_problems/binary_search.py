a = [4,3,2,6,66,8,90,2,3]
sorted = list(set(a))
sorted.sort()
print(sorted)


b = int(input("enter number you want to search: "))

first_ind = 0
last_ind = len(sorted) - 1



while first_ind <= last_ind:
  mid_ind = (first_ind + last_ind ) // 2
  if sorted[mid_ind] == b:
    print(f"{sorted[mid_ind]} found at index {mid_ind}")
    break
  else:
    if sorted[mid_ind] > b:
      last_ind = mid_ind -1 
      
    else:
      first_ind = mid_ind + 1


else:
  print("Not found")