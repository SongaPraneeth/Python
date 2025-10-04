with  open(input("enter a file name -> "), "r") as f:
  count = 0
  for line in f:
    count += 1
  print(count)
