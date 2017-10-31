while True:
    my_string = input('Enter input string:\n')
    if(my_string == 'q'):
        break
    
    elif(my_string.find(',') == -1):
        print('Error: No comma in string.\n')
        
    else:
        my_list = my_string.split(',')
        print ('First word:',my_list[0].strip())
        print ('Second word:',my_list[1].strip())
        print('\n')
