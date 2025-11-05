import string

upper_letter = list(string.ascii_uppercase)
lower_letter = list(string.ascii_lowercase)


ciphertext = input("enter the cipher text: ")
key = input("Enter the key: ")
key_small = key.lower()

plain_text = ''

for i in ciphertext:
  if i.islower():
    indexinkeysmall = key_small.index(i)
    plain_text += lower_letter[indexinkeysmall]
  
  elif i.isupper():
    indexinkey = key.index(i) 
    plain_text += upper_letter[indexinkey]
    
  else:
    plain_text += i
    
    
print(plain_text)