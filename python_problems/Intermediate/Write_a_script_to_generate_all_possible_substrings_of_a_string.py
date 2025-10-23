def sub_string(n):
  print(n)
  print(len(n))
  
  for i in range(len(n)):
      j = 0
      j += i
      while j < len(n) :
        print(n[i:i+j+1])
        j += 1


a = input("Enter a string and sub strings will be printed: ")
sub_string(a)