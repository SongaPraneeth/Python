import re
import base64

def one_of_hex_base64_plain(n):
  try :
    base64.b64decode(n,validate=True)
    print("IT is a base64")
    return
  except Exception:
    pass

  try :
    
    int(n,16)
    print("IT is a hex")
    return
    
  except ValueError:
    pass

  if re.fullmatch(r"[A-Za-z0-9@!#$%^&*()]+",n):
    print("plain text")
    return
  

  print("not a base , hex or plain")
 

  


A = input("enter a string to detect, is the given string is hex, base64 or plain text: ")
one_of_hex_base64_plain(A)

