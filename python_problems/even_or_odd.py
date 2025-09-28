def even_odd():
  di = int(input("enter a number: "))

  if di % 2 == 0 :
    print("Even")
  else :
    print("odd")

even_odd()


'''chat gpt given code 

def even_odd(n: int) -> str:
    return "Even" if n % 2 == 0 else "Odd"

# usage
num = int(input("Enter a number: ").strip())
print(even_odd(num))

'''