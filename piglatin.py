string = input("English: ")
s = string.split()

piglatin = ""

for word in s:
  piglatin = piglatin + word[1:] + word[0] +"AY "
  
piglatin = piglatin[:-1]

print("Pig Latin:",piglatin)
