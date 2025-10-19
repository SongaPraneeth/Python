import re

with open(input("enter a file: "))as f:
  a = f.read()
  finding_ip = re.findall(r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+",a)

dup = {}

for i in finding_ip:
  if i in dup:
    dup[i] += 1
  else:
    dup[i] = 1

print(dup)

