password_users = {}


with open(input("Enter the file name: ")) as f:
  next(f)
  
  for line in f:
    line = line.strip()

    if not line:
      continue
    
    username, password, *rest = line.split(",")
    
    if password not in password_users:
      password_users[password] = []
    password_users[password].append(username)

for password, users in password_users.items():
  if len(users) > 1:
    print(f"users with duplicate password '{password}': {';'.join(users)}")