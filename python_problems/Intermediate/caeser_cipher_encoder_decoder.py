small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

decide = input("Enter A for encode, B for decode: ")

strings = input("Enter the String: ")
key = int(input("Enter a key: "))



if decide == 'A':
  encode = ""

  for i in strings:
    if i in small:
      index = (small.index(i) + key ) % 26
      encode = encode + small[index]
    else:
      index = (capital.index(i) + key ) % 26
      encode = encode + capital[index]

  print("Encoded value is: ",encode)



elif decide == 'B':
  decode = ""

  for i in strings:
    if i in small:
      index = (small.index(i) - key ) % 26
      decode = decode + small[index]
    else:
      index = (capital.index(i) - key) % 26 
      decode = decode + capital[index]

  print("Encoded value is: ",decode)