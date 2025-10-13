def fab(n: int) -> int:
  a=0
  b=1
  c = 0
  for _ in range(n):
    print(a)
    a = a + b
    b = c
    c = a

z = int(input('enter a numver for how many number you want to print:'))
fab(z)




# def fab(n: int) -> None:
#     a, b = 0, 1
#     for _ in range(n):
#         print(a)
#         a, b = b, a + b
