def duplicate_element_finder(n):
  seem = []
  duplicate = []
  for i in n:
    if i in seem:
      if i not in duplicate:
        duplicate.append(i)

    else:
      seem.append(i)
  print(duplicate)


w = list((input("enter numbers or characters with spaces:").split()))
duplicate_element_finder(w)