def find_string(string, sub_string):
  rm = 0
  for i in range(0, len(string)):
    if string[i:i+len(sub_string)] == sub_string :
      rm = rm +1

  return rm

string = input("enter the string:")
sub_string = input("enter the sub_string:")

print(find_string(string,sub_string))


#for i range(len(string) - (len(sub_string)+1) ): /// this will stop  exactly after the last full substring can fit,


#hello
def find_string(string, sub_string):
  rm = 0
  for i in range(0, len(string)):
    if string[i:i+len(sub_string)] == sub_string :
      rm = rm +1

  return rm

string = input("enter the string:")
sub_string = input("enter the sub_string:")

print(find_string(string,sub_string))