#it will not run for 0 factorial

def facti(z: int) -> int:
  
  for i in range(1,z):
    z = i *z
  return z
    

it = int(input('enter a number: '))
print(facti(it))




# def facti(z: int) -> int:
#     a = 1
#     for i in range(1, z+1):
#         a = a * i
#     return a