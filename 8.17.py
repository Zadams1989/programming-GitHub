team={}
for i in range(5):
    jersey=int(input("Enter player %s's jersey number:\n" % str(i+1)))
    rating=int(input("Enter player %s's rating:\n" % str(i+1)))

    if jersey not in team:
        team[jersey]=rating
    print()

print("ROSTER")
for k,v in sorted(team.items()):
    print("Jersey number: %d,Rating: %d" % (k,v))

print()

while True:

    print('\na - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')

    choice=input('\nChoose an option:\n')

    choice=choice.lower()

  
    if choice=='o':

        print("\nROSTER")
        for k,v in sorted(team.items()):
            print("Jersey number:%d, Rating:%d" % (k,v))

    elif choice=='a':

        jersey=int(input("Enter a new player jersey number:\n"))
        rating=int(input("Enter player's rating:\n"))

        if jersey not in team:
            team[jersey]=rating
        else:
            print("\nThe Player already in the list")

    elif choice== 'd':

        jersey=int(input("\nEnter a jersey number:\n"))

        if jersey in team:
            del d[jersey]
        else:
            print("\nThe Player is not in the list")

    elif choice== 'u':

        jersey=int(input("\nEnter a jersey number:\n"))

        if jersey in team:
            rating=int(input("\nEnter a new rating for the player:\n"))
            team[jersey]=rating
        else:
            print("\nThe Player is not in the list")

    elif choice== 'r':
      

        rating=int(input("\nEnter a rating:\n"))

        for k,v in sorted(team.items()):

            if v > rating:
                print("Jersey number:%d,Rating:%d" % (k,v))

    elif choice=='q':
        break
    else:
        print("\nEnter a valid choice")
