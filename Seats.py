#creating a function for the seat booking


# hello, please enter your name.
# these are the available movies today
# these are the available sessions
# this is the available seating

seating_choice = None
#option 2
movie1_seats = ([],[],[])
movie2_seats = ([],[],[])
movie3_seats = ([],[],[])

def book_seating(movie_seats,session_index):
    #testing (we have booked seat number 2)
    movie_seats[session_index].append(2)
    seat_txt = ''
    for seat_number in range(1,16):
        if seat_number in movie_seats[session_index]:
            seat_txt = seat_txt + 'x '
        else:
            seat_txt = seat_txt + str(seat_number) + ' '
    seating_choice = None
    
    #my rubbish attempts at coding
    while movie_seats not in 
        if movie_seats > 1:


    print(seat_txt)
    return seating_choice

book_seating(movie1_seats, 1)