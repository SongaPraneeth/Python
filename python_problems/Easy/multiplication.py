def mul(n: int) -> int:
  i = 1
  while i < 11:
    print(f"{n} x {i} = {n*i}")
    i += 1


i = int(input("enter a number: "))
mul(i)