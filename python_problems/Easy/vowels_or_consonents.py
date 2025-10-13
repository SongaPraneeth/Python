def vow_con(n: str):
  z = list(n)
  z = n.lower()
  
  a=0
  b=0
  for i in range(len(z)):
    if (z[i] == 'a') or (z[i] == 'e') or (z[i] == 'i') or (z[i] == 'o') or (z[i] == 'u'):
      a = a+1
    else:
      b = b + 1
  print("number of vowels are: ",a)
  print("number of consonetns are: ",b)

take = input("Enter a string: ").strip()
vow_con(take)



# Things to note / improvements:

# Case sensitivity

# Your code only counts lowercase vowels ('a', 'e', 'i', 'o', 'u').

# If the user enters uppercase letters, they’ll all be counted as consonants.

# Fix: convert input to lowercase:

# z = n.lower()


# Non-alphabetic characters

# Spaces, digits, punctuation are currently counted as consonants.

# You might want to check only alphabetic characters:

# if z[i].isalpha():
#     if z[i] in 'aeiou':
#         a += 1
#     else:
#         b += 1


# Pythonic version

# def vow_con(n: str):
#     n = n.lower()
#     vowels = sum(1 for c in n if c in 'aeiou')
#     consonants = sum(1 for c in n if c.isalpha() and c not in 'aeiou')
#     print("Number of vowels:", vowels)
#     print("Number of consonants:", consonants)