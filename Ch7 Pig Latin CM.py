print('Enter text to be translated (All capital letters. ', end='')
text = input('No punctuation):\n')

split_text = text.split()

for word in split_text:
    word = word[1:] + word[0] + 'AY'
    print(word, end=' ')
