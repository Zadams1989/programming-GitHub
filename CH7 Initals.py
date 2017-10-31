name = input("Enter name: ")

name = name.split()

short = ""

for i in range(len(name)):
  short = short + name[i][0]+"."
  
print(short)
