
print("Welcome to Cinemaplex!")

movie_choices = {'01': 'The Batman','02':'Turning Red', '03':'Spiderman: No Way Home'}
sessions = {'01':'10AM','02':'3PM', '03':'6PM'}

name = None
movie_order = None
seating_choice = None
number = None

name = input("Please enter your name:  ")
print(name)
    
number = int(input("Please enter your phone number:  "))

order = {}

#booking the movie.
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

print("Please choose a movie to watch.")
for code, choice in movie_choices.items():
    print (code, '->', choice)

print()


#validate the starter
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

#validate the starter
while session_order not in sessions.keys():
    session_order = input ('Please, enter the session code: ')
    if session_order not in sessions:
        print('Wrong session code.')
    else:
        order[session_order] = sessions[session_order]

#creating a function for the seat booking

# hello, please enter your name.
# these are the available movies today
# these are the available sessions
# this is the available seating

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
movie_seats[session_order].append(2)

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
        seating_choice = int(input('Please, choose your seat: '))
        
    except:
        print ("Wrong seat")
        seating_choice = None

