encoded_str = input("Enter the encoded base64 to check for padding: ")



if len(encoded_str) % 4 != 0:
  encoded_str += '=' * (4 -len(encoded_str)%4)
  
print(encoded_str)



