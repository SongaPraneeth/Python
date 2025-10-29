import re
urls = [
    "https://www.google.com/search?q=python",
    "http://example.org/about",
    "https://subdomain.amazon.co.uk/products",
    "ftp://files.server.net/downloads/file.zip",
    "https://openai.com/research/",
    "http://blog.medium.com/articles",
    "https://mail.yahoo.co.jp/inbox",
    "https://www.github.com/user/repo",
    "http://news.bbc.co.uk/world",
    "https://www.wikipedia.org/wiki/Artificial_intelligence",
    "https://docs.python.org/3/library/urllib.parse.html",
    "http://localhost:8000/test",
    "https://mywebsite.io/contact",
    "https://login.microsoftonline.com/",
    "http://192.168.1.10/dashboard"
]

pattern = r"(?:[A-Za-z0-9-]+\.)+[a-zA-Z]{2,}|[A-Za-z0-9-]+\.[a-z]+|[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+|localhost(?::\d+)?" 


for i in urls:
  domain = re.findall(pattern,i)
  if domain:
    print(domain)
  



   
