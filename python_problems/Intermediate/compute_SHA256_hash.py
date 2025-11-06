import textwrap


MASK32 = 0xFFFFFFFF

def rotr(x,n):
  return ((x>>n) | (x << (32 -n))) & MASK32 

def shr(x,n):
  return x >> n





msg = input("Enter a value: ")
ascii_value = []
binary_value = []
binary_value_str = ''

#converting text to ascii value
for i in msg:
  ascii_value.append(ord(i))
  # print(f"Ascii value: {ascii_value}")
  # print()

# convertin ascii value to binary 8-bit value and keeping in a list
for i in ascii_value:
  binary_value.append(format(i,"08b"))
  # print(f"Binary (8-bit): {binary_value}")
  # print()
    
# Joining all 8-bit binary value in a list to single string
for i in range(len(binary_value)):
  b = binary_value[i]
  binary_value_str += b
  
  # padding 1 at the end of the binary value 
binary_value_str += '1'

  # padding 0 until the length of the binary value divide 512 and remainder is 448 
while len(binary_value_str)%512 != 448:
  binary_value_str += '0'

# print(f"Before final pading: {binary_value_str}")
# print()

# print(f"Before final pading lenght: {len(binary_value_str)}")
# print()

# converting the original lenght of the message to 64 bit binary value and adding it to the binary value making it the 512 bit binary value
message_len = len(msg) * 8
message_length_bin = format(message_len,"064b")
binary_value_str += message_length_bin

# print(f"final padding: {binary_value_str}")
# print()

# print(f"Total length : {len(binary_value_str)}")



H = [
    0x6a09e667,
    0xbb67ae85,
    0x3c6ef372,
    0xa54ff53a,
    0x510e527f,
    0x9b05688c,
    0x1f83d9ab,
    0x5be0cd19]






k = [
  0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
  0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
  0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
  0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
  0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
  0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
  0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
  0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
  0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
  0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
  0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
  0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
  0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
  0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
  0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
  0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
  ]

chunks = textwrap.wrap(binary_value_str, 512)

for chunk in chunks:
  W = textwrap.wrap(chunk,32)
  W = [int(w,2) for w in W]
  # print(W)
  # print(len(W))

  for i in range(16, 64):
    sigma0 = rotr(W[i-15],7) ^ rotr(W[i-15],18) ^ shr(W[i-15],3)
    sigma1 = rotr(W[i-2],17) ^ rotr(W[i-2],19) ^ shr(W[i-2],10)
    W.append((W[i-16] + sigma0 + W[i-7] + sigma1) & MASK32)
    
  # print(W)





  a, b, c, d, e, f, g, h = H



  for i in range(64):
    Σ1 = rotr(e,6) ^ rotr(e,11) ^ rotr(e,25)
    ch = (e & f) ^ ((~e & MASK32) & g)
    T1 = (h + Σ1 + ch + k[i] + W[i]) & MASK32


    Σ0 = rotr(a,2)^ rotr(a,13) ^ rotr(a,22)
    maj = (a & b) ^ (a & c) ^ (b & c)
    T2 = (Σ0 + maj) & MASK32

    h = g
    g = f
    f = e
    e = (d + T1) & MASK32
    d = c
    c = b
    b = a
    a = (T1 + T2) & MASK32

  H = [ (H[0] + a) & MASK32,
          (H[1] + b) & MASK32,
          (H[2] + c) & MASK32,
          (H[3] + d) & MASK32,
          (H[4] + e) & MASK32,
          (H[5] + f) & MASK32,
          (H[6] + g) & MASK32,
          (H[7] + h) & MASK32  ]

  # print(H)
  # print()


final_hash = ''.join(f"{x:08x}" for x in H)

print("\nSHA-256:", final_hash)