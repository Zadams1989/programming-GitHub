string = input('Enter input string:\n')

while string != 'q':
    if ',' not in string:
        print('Error: No comma in string.\n')
        string = input('Enter input string:\n')

    else:
        split_string = string.split(',')
        first_word = split_string[0]
        first_word = first_word.strip()
        second_word = split_string[1]
        second_word = second_word.strip()
        print('First word:', first_word)
        print('Second word:', second_word)
        print('')
        string = input('Enter input string:\n')
