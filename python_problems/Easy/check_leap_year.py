import calendar
a = int(input("Enter a year: "))

if calendar.isleap(a):
  print("It is leap year")

else:
  print("Not a leap year")
