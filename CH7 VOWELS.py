def count_vowels(text):
    c=0

text=text.lower()

for x in text:

if x in 'aeiou':

c=c+1

return c



def count_consonants(text):

c=0

text=text.lower()

for x in text:

if x not in 'aeiou' and str.isalpha(x):

c=c+1

return c



def main():

text=input("Enter String:")

vowels = count_vowels(text)

consonants = count_consonants(text)

print("Number of Vowels in inputted string is: "+str(vowels))

print("Number of Consonants in inputted string is: "+str(consonants))
