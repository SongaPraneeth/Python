def func(z: str) -> str:
  temp = z
  if temp == z[::-1] :
    return 'palindrome'
  else:
    return 'not a palindrome'
  
w = input('enter a string: ')
print(func(w))



# def reverse_string(s: str) -> str:
#     rev = ""
#     for ch in s:         # loop over each character
#         rev = ch + rev   # add it to the front
#     return rev
