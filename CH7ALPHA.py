def toPhoneNumber(str):
   str=str.replace("A", "2")
   str=str.replace("b", "2")
   str=str.replace("C", "2")
  
   str=str.replace("D", "3")
   str=str.replace("E", "3")
   str=str.replace("F", "3")
  
   str=str.replace("G", "4")
   str=str.replace("H", "4")
   str=str.replace("I", "4")
  
   str=str.replace("J", "5")
   str=str.replace("K", "5")
   str=str.replace("L", "5")
  
   str=str.replace("M", "6")
   str=str.replace("N", "6")
   str=str.replace("O", "6")
  
   str=str.replace("P", "7")
   str=str.replace("Q", "7")
   str=str.replace("R", "7")
   str=str.replace("S", "7")
  
   str=str.replace("T", "8")
   str=str.replace("U", "8")
   str=str.replace("V", "8")
  
   str=str.replace("W", "9")
   str=str.replace("X", "9")
   str=str.replace("Y", "9")
   str=str.replace("Z", "9")

   return str
  
str=input("Enter a phone number to be translated: ")
print(toPhoneNumber(str))
