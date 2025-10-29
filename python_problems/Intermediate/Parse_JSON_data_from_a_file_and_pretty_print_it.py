import json

with open("d:\python\python_problems\Intermediate\data.json","r") as file:
  data = json.load(file)


  with open("d:\python\python_problems\Intermediate\corrected.json","w") as outfile:
    json.dump(data, outfile, indent=2)