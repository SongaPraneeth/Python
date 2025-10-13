import re

a = input("Enter a sentence with email:")

b = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",a)

print(b)