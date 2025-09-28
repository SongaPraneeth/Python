def rev(n: str) -> str:
  x = list(n)
  print(len(x))
  for i in range(len(x)//2):
    temp = x[i]
    x[i] = x[len(x) - 1 - i]
    x[len(x) - 1 - i] = temp

  return ''.join(x)

#  def rev(n: str) -> str:
#    return n[::-1]  




sti = input("Enter a string:").strip()

print(rev(sti))