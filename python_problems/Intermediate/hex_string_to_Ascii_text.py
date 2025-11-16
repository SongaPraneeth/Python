hex_value = input("enter the hex value: ").split() # Take a space-separated hex string as input and split it into individual hex values

ASCII_TEXT = ''  

for i in hex_value:        
  decimal = int(i,16)      # Converting each hex string to decimal integer
  char = chr(decimal)      # Convert the decimal value to its corresponding ASCII character
  ASCII_TEXT += char      # Append the character to the final output string
  
print(ASCII_TEXT)         # Print the final ASCII text