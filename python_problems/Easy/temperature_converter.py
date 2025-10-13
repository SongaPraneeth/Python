try: 

  def conv(tell):
      if tell == 1:
        cel = float(input("enter the celsius temperature you want to convert: "))
        far = (cel*9/5)+32
        print(f"{cel}°C = {far}°F")

      else:
        far = float(input("enter the fahrenheit temperature you want to convert: "))
        cel = (far-32)*5/9
        print(f"{far}°F = {cel}°C")


  tell = int(input("in which temperature you want to convert choose option 1 or 2 \n1.celsius to fahrenheit \n2.fahrenheit to celsisus\n: "))

  if tell in [1,2]:
    conv(tell)

  else:
    print("Please enter option 1 or 2")


except ValueError:
  print("Please enter option 1 or 2")




  