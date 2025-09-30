def sorting(n: list) -> list:
  z = 0
  while len(n) > z:
    for i in range(len(n)-1):
      if n[i] > n[i+1] :
        temp = n[i]
        n[i] = n[i+1]
        n[i+1] = temp
    z = z + 1
  return n
  

n= list(map(int,input("enter numbers separeted by a space : ").split()))
print(sorting(n))






