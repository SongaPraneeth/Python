import textwrap

decide = input("enter-> A for encode, B for decode: ")

base64_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
if decide == "A": 
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




elif decide == "B" : 

  def remove_padding(n1):
    z=[]
    for i in n1:
      if i != '=':
        z.append(i)
    print(z)
    base64char_to_decimal(z)
  
  def base64char_to_decimal(n2):
    decimal = []
    for i in n2:
      decimal.append(base64_characters.index(i))
    
    print(decimal)
    decimal_to_6_bit(decimal)

  def decimal_to_6_bit(n3):
    binary = []
    for i in n3:
      binary.append(format(i,'06b'))

    print(binary)
    six_bit_to_8bit(binary)
  def six_bit_to_8bit(n4):
    eight_bit = ''
    for i in n4:
      eight_bit += i
    eight_bit = textwrap.wrap(eight_bit,8)
    print(eight_bit)
    eight_bit_to_decimal_to_ascii(eight_bit)

  def eight_bit_to_decimal_to_ascii(n5):
    ascii_val = ''
    for i in n5:
      decimal = int(i,2)
      ascii_val += chr(decimal)

    print(ascii_val)

  b = list(input("Enter the encoded string: "))
  remove_padding(b)




else: 
  print("Please enter A or B")