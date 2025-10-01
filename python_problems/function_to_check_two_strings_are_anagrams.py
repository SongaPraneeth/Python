# An anagram is when you take the letters of one word (or phrase) and rearrange them to form another valid word (or phrase), using all the original letters exactly once. example: listen silent



def check_anagram(x,y : str) -> str:
  if len(x) != len(y):
    return print("Not a anagram")
  
  freq_x = {}
  freq_y = {}

  for i in x:
    if i in freq_x:
      freq_x[i] += 1
    else:
      freq_x[i] = 1

  for i in y:
    if i in freq_y:
      freq_y[i] += 1
    else:
      freq_y[i] = 1
  
  if freq_x == freq_y :
    print("its a anagram")
  else:
    print("not a anagram")

a , b = input("enter two words with space to check if they are anagram: ").split()
check_anagram(a,b)