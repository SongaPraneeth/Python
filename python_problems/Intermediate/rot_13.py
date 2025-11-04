small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']





plain_text = input("Enter a string: ")

rot_13_encoded_text = ''
for i in plain_text:
  if i in small:
    index = small.index(i) 
    rot_13_encoded_text += small[(index + 13)%26]
  elif i in capital:
    index = capital.index(i)
    rot_13_encoded_text += capital[(index + 13)%26]
    
    
print(rot_13_encoded_text)

