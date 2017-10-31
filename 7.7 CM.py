title = input('Enter a title for the data:\n')
print('You entered:', title)
print('')
column1 = input('Enter the column 1 header:\n')
print('You entered:', column1)
print('')
column2 = input('Enter the column 2 header:\n')
print('You entered:', column2)
print('')
user_data = input('Enter a data point (-1 to stop input):\n')
datapoint1 = []
datapoint2 = []

while user_data != '-1':
    if ',' not in user_data:
        print('Error: No comma in string.\n')
        user_data = input('Enter a data point (-1 to stop input):\n')
    elif user_data.count(',') > 1:
        print('Error: Too many commas in input.\n')
        user_data = input('Enter a data point (-1 to stop input):\n')
    else:
        split_data = user_data.split(',')
        data1 = split_data[0]
        data1 = data1.strip()
        data2 = split_data[1]
        data2 = data2.strip()
        if data2.isdigit() == False:
            print('Error: Comma not followed by an integer.\n')
            user_data = input('Enter a data point (-1 to stop input):\n')
        else:
            datapoint1.append(data1)
            data2 = int(data2)
            datapoint2.append(data2)
            print('Data string:', data1)
            print('Data integer:', data2)
            print('')
            user_data = input('Enter a data point (-1 to stop input):\n')
print('')
print('%33s' % title)
print('%-20s|%23s' % (column1, column2))
print('-' * 44)
i = 0
for author in datapoint1:
    print('%-20s|%23d' % (author, datapoint2[i]))
    i = i + 1
print('')
k = 0
for writer in datapoint1:
    print('%20s' % writer, '*' * datapoint2[k])

