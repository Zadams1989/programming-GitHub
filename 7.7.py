mylist1 = []
mylist2 = []

var = input("Enter a title for data: ")
print ("You entered: ", var)
head1 = input("Enter the column 1 header: ")
print ("You entered: ", head1)

head2 = input("Enter the column 2 header: ")
print ("You entered: ", head2)
counter = 0
while True:
    value = input("Enter a data point(-1 to stop input): ")
    if value == "-1":
        break
    else:
        for c in value:
            if(c == ','): counter +=1
        if(counter <= 0):
            print ('Error: No comma in string')
        elif(counter >=2):
            print('Too many commas in input')
        else:
            val,num = value.split(',')
            try:
                int(num)
                mylist1.append(val)
                mylist2.append(num)
                print ("Data string: ", val)
                print ("Data integer: ", num)
            except ValueError:
                print('Comma not follwed by integer')
    counter = 0
print ('%s' % (var.rjust(33)))
print ('%12s |%12s' % (head1.ljust(20), head2.rjust(23)))
print ('---------------------------------------------')
for i in range(len(mylist1)):
   print ('%12s |%12s' % (mylist1[i].ljust(20), mylist2[i].rjust(23)))
