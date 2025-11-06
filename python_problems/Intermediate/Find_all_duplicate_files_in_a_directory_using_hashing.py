import hashlib
import os

directory_path = input("Enter the directory path: ")  

dic = {}

for contents in os.listdir(directory_path):               # loops through all items files in the directory
  
  file_path = os.path.join(directory_path,contents)       #  creates the full path to the file by joining directory path and file name
  with open(file_path,"rb") as f:                         # opens the file and reads as binary
    a = f.read()                                          # reads the file
    sha256_hash = hashlib.sha256()                        # creates a new SHA-256 hash object
    sha256_hash.update(a)                                 # feeds the file content (bytes) into the hash object
    dic[contents] = sha256_hash.hexdigest()               # stores filename as key and its SHA-256 hash (in hex string form) as value

# print(dic)  

values = list(dic.values())

seems = []
duplicates = []

for i in values:                                 # appends duplicte values in duplicate variable
  if i not in  seems:
    seems.append(i)
  else:
    duplicates.append(i)
    
for dup in duplicates:                            # prints all duplicates files in separate lists
  duplicate_files = []
  for key,value in dic.items():
    if value == dup:
      duplicate_files.append(key)
  print(duplicate_files)                   
