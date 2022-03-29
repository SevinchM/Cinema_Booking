def booking():

    print("Welcome to Cinemaplex!")

    print("You may order a movie session and book seats here!")

    print()
    #creating dictionaries for the available movies and sessions
    movie_choices = {'01': 'The Batman','02':'Turning Red', '03':'Spiderman: No Way Home'}
    sessions = {'01':'10AM','02':'3PM', '03':'6PM'}

    #creating the variables
    name = None
    movie_order = None
    seating_choice = None
    number = None

    #Input the name of the person booking.
    name = input("Please enter your name:  ")
    print("Booking under name: ", name)
    
    print()
    #Entering the phone number of the person booking. 
    number = int(input("Please enter your phone number:  "))

    #validating the user input(phone number)
    if type(number) == int:
        print("Pnone number: ", number)
    else:
        print("Invalid number entered.")
    order = {}

    #booking the movie.
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

    print("Please choose a movie to watch.")
    for code, choice in movie_choices.items():
        print (code, '->', choice)

    print()


    #validate the movie code
    while movie_order not in movie_choices.keys():
        movie_order = input ('Please, enter the movie code: ')
        if movie_order not in movie_choices:
            print('Wrong movie code.')
        else:
            order[movie_order] = movie_choices[movie_order]

    #booking the session
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

    print("Please choose a viewing session")
    for code, choice in sessions.items():
        print (code, '->', choice)

    print()
    session_order = None

    #validating the session order
    while session_order not in sessions.keys():
        session_order = input ('Please, enter the session code: ')
        if session_order not in sessions:
            print('Wrong session code.')
        else:
            order[session_order] = sessions[session_order]

    #creating a function for the seat booking


    #Seats for each movie.
    movie1_seats = {'01':[],'02':[], '03':[]}
    movie2_seats = {'01':[],'02':[], '03':[]}
    movie3_seats = {'01':[],'02':[], '03':[]}

    match movie_order:
        case '01':
            movie_seats = movie1_seats
        case '02':
            movie_seats = movie2_seats
        case '03':
            movie_seats = movie3_seats
        
    #testing (we have booked seat number 2)

    print()

    print("These are the available seats.")
    seat_txt = ''
    for seat_number in range(1,16):
        if seat_number in movie_seats[session_order]:
            seat_txt = seat_txt + 'x '
        else:
            seat_txt = seat_txt + str(seat_number) + ' '
    print(seat_txt)

    print("Please choose your seat.")

    seating_choice = None
    while seating_choice not in range(1,16):
        try:
            seating_choice = int(input('Select seat: '))
            
        except:
            print ("Wrong seat")
            seating_choice = None

    movie_seats[session_order].append(seating_choice)


    print()
    seat_txt = ''
    for seat_number in range(1,16):
        if seat_number in movie_seats[session_order]:
            seat_txt = seat_txt + 'x '
        else:
            seat_txt = seat_txt + str(seat_number) + ' '
    print("Your seating:")
    print(seat_txt)

    print()

    print(f"Your full order: {movie_order},{session_order},{seating_choice}")

    print()
    place_order = ''


    while place_order.lower() not in ('yes', 'no'):
        place_order = input ('Would you like to place your order (yes/no)? ')

    if place_order == 'yes':
        print ('Your order is being processed')
    else:
        print ('Your order has been cancelled')

    print()
    new_order = ''

    while new_order.lower() not in ('yes', 'no'):
        new_order = input ('Would you like to book again (yes/no)? ')

    if new_order == 'yes':
        booking()
    else:
        print("Thank you for using our services!")
        
booking()