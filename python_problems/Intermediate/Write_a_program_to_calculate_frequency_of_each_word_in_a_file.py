import string

with open(input("enter the file name: "), "r") as f:
  a = f.read()
  
  puntuation_chrs = string.punctuation
  
  without_puntuation = ''
  
  for i in a:
    if i not in puntuation_chrs:
      without_puntuation += i

  freq = {}
  without_puntuation = without_puntuation.split()
  for i in without_puntuation :
    if i in freq:
      freq[i] += 1
    else: 
      freq[i] = 1
      
  for word,count in freq.items():
    print(f"{word}:{count}")