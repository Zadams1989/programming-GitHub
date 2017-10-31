user_string = input('Enter string of text:\n')

def num_vowels(text=user_string):
    i = 0
    text = text.lower()
    for vowel in text:
        if vowel in 'aeiou':
            i += 1

    return i

def num_consonants(text=user_string):
    i = 0
    text = text.lower()
    text = text.replace(' ', '')
    for consonant in text:
        if consonant not in 'aeiou':
            i += 1
    return i

print('Number of vowels in your string:', num_vowels())
print('Number of consonants in your string:', num_consonants())

