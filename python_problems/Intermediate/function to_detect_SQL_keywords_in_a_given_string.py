

def sql_key(n):
  sql_keywords = [
    "SELECT", "FROM", "WHERE", "INSERT", "UPDATE", "DELETE", "CREATE",
    "DROP", "ALTER", "TABLE", "JOIN", "INNER", "LEFT", "RIGHT",
    "FULL", "ON", "AS", "DISTINCT", "ORDER", "BY", "GROUP", "HAVING",
    "LIMIT", "OFFSET", "VALUES", "INTO", "AND", "OR", "NOT", "NULL",
    "PRIMARY", "KEY", "FOREIGN", "REFERENCES", "INDEX", "VIEW", "DATABASE"
  ]
 
  found = []
  for i in n:
    if i.upper() in sql_keywords:
      found.append(i)
  
  print(f"SQL Keywords found:{found}")


a = input("Enter a string: ").split()
sql_key(a)