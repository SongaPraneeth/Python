import textwrap

base64_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def string_ascii(n1):
  a_v = []
  for i in n1:
    ascii_value = ord(i)
    a_v.append(ascii_value)
  print("ASCII values: ",a_v)
  ascii_binary(a_v, len(n1))

def ascii_binary(n2, input_lenght):
  binary = ''
  for i in n2:
    binary  = binary + format(i, '08b' )
  print("Binary string: ",binary)

  while len(binary)%6 != 0:
    binary += '0'
  binary_sixbit(binary,input_lenght)

def binary_sixbit(n3,input_length):
  six_bits = textwrap.wrap(n3,6)
  print("6-bit chunks: ",six_bits)
  sixbit_decimal(six_bits,input_length)

def sixbit_decimal(n4,input_length):
  decimal = []
  for i in n4: 
    decimal.append(int(i,2))
  print("Decimal values: ",decimal)
  decimal_base64(decimal,input_length)

def decimal_base64(n5,input_length):
  
  base64_encoded = ''
  for i in n5:
    base64_encoded = base64_encoded + base64_characters[i] 
  
  
  padding = (3- input_length % 3) % 3
  base64_encoded += '=' * padding
  print("Base64 Encoded: ",base64_encoded)



  
    
    
    
    















a= input("Enter a string: ")
string_ascii(a)