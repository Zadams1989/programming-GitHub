username = input('Enter you first, middle and last name:\n')

while username != 'abort':
    if ' ' not in username:
       print('Error. Enter first, middle and last name separated by spaces.\n')
       username = input('Enter you first, middle and last name:\n')
    elif username.count(' ') < 2:
       print('Error. Less than three names detected.\n')
       username = input('Enter you first, middle and last name:\n')
    else:
       split_names = username.split(' ')
       username = 'abort'

for name in split_names:
    name = name.strip()
    print('%s. ' % name[0], end='')
