import re
import urllib.request

url = input("enter a html page: ")
with urllib.request.urlopen(url) as data:
  r = data.read().decode("utf-8")

b = re.findall(r"https?://[A-Za-z0-9./_%+:-]+",r)
  
print("urls found:")
for i in b:
  print(i)