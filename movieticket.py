from datetime import datetime

users_data =[]
bookings =[]
movies_list =[]
theatres_details =[]
show_time_details = []

class Movies:

    def __init__(self, movie_id: int, movie_name: str, duration: str, rating: float):

        self.movie_id = movie_id
        self.movie_name = movie_name
        self.duration = duration
        self.rating = rating

class Theatres:
    
    def __init__(self, theatre_id: int, theatre_name, location, rating, seats):

        self.theatre_id = theatre_id
        self.theatre_name = theatre_name
        self.location = location
        self.rating = rating
        self.seats = seats

   
class Show_time:

    def __init__(self, show_id, show_time):
        
        self.show_id = show_id
        self.show_time = show_time
        
class Users:

    def __init__(self, user_id: int, user_name: str, email_id: str, password: str, user_role: str):

        self.user_id = user_id
        self.user_name = user_name
        self.email_id = email_id
        self.password = password
        self.user_role = user_role

    def hard_code_data(self):

        users_data.append(self)

    def greetings(self):
        print("Welcome User!", self.user_name)

    def validate_user(self, email_id, password):

        for users in users_data:
            if users.email_id == email_id and users.password == password:
                return users
        return None
    

class Ticket_booking(Users):

    def __init__(self,user_id, user_name, email_id, password, user_role):
        super().__init__(user_id, user_name, email_id, password, user_role)

        self.booking_history = []

    def display_menu(self):
        stay_in_menu = True
        while stay_in_menu:
            print("--------------------------------------------------------\n")
            print("1. Book Movie")
            print("2. Display Booking history")
            print("3. Delete Booking history")
            print("4. Logout")
            print("--------------------------------------------------------\n")

            choice = int(input("Enter your choice: "))
        
            if choice == 1:    
                movie1 = Movies(1, "Por Thozhil", "2hr 27mins", 7.5)
                movie2 = Movies(2, "Pichaikaran", "2hr 30mins", 6.2)
                movie3 = Movies(3, "Takkar", "2hr 21mins", 6.8)
                movies_list.append(movie1)
                movies_list.append(movie2)
                movies_list.append(movie3)
       
                for movie in movies_list:
                    print(movie.movie_id, "\t", movie.movie_name, "\t", movie.duration, "\t", movie.rating)
                print("--------------------------------------------------------\n")
                movie_id = int(input("Enter the Movie Id to book: "))
                selected_movie = None
                for movie in movies_list:
                    if movie.movie_id == movie_id:
                        selected_movie = movie
                        break
                if selected_movie is None:
                    print("Invalid Movie Id ")
                else:
                    theatre1 = Theatres(1, "PVR Cinemas    ", "Anna Nagar", 7.5, [["A1", "A2", "A3", "A4", "A5"], ["B1", "B2", "B3", "B4", "B5"], ["C1", "C2", "C3", "C4", "C5"],["D1", "D2", "D3", "D4", "D5"]])
                    theatre2 = Theatres(2, "AGS Cinemas    ", "Villivakkam", 6.2, [["A1", "A2", "A3", "A4", "A5"], ["B1", "B2", "B3", "B4", "B5"], ["C1", "C2", "C3", "C4", "C5"],["D1", "D2", "D3", "D4", "D5"]])
                    theatre3 = Theatres(3, "Rohini Cinemas","Koyambedu", 6.8, [["A1", "A2", "A3", "A4", "A5"], ["B1", "B2", "B3", "B4", "B5"], ["C1", "C2", "C3", "C4", "C5"],["D1", "D2", "D3", "D4", "D5"]])
                    theatres_details.append(theatre1)
                    theatres_details.append(theatre2)
                    theatres_details.append(theatre3)
       
                    for theatre in theatres_details:
                        print(theatre.theatre_id, "\t", theatre.theatre_name, "\t", theatre.location, "\t", theatre.rating)

                    print("--------------------------------------------------------\n")
                    theatre_id = int(input("Enter the Theatre Id to see show time: "))
                    selected_theatre = None
                    for theatre in theatres_details:
                        if theatre.theatre_id == theatre_id:
                            selected_theatre = theatre
                            break
                    if selected_theatre is None:
                        print("Invalid Theatre Id ")
                    else:
                        show_time1 = Show_time(1, "09:30 AM")
                        show_time2 = Show_time(2, "01:00 PM")
                        show_time3 = Show_time(3, "04:30 PM")
                        show_time4 = Show_time(4, "10:00 PM")
                        show_time_details.append(show_time1)
                        show_time_details.append(show_time2)
                        show_time_details.append(show_time3)
                        show_time_details.append(show_time4)

                        for show in show_time_details:
                            print(show.show_id, "\t", show.show_time)
                        
                        print("--------------------------------------------------------\n")
                        show_id = int(input("Enter the Show id: "))
                        selected_show = None
                        for show in show_time_details:
                            if show.show_id == show_id:
                                selected_show = show
                                break
                        if selected_show is None:
                            print("Invalid Show Id ")
                        else:
                            for seats in selected_theatre.seats:
                                print(seats)
                            print("--------------------------------------------------------\n")
                            seat = input("Select seats: ").upper().split(" ")
                            selected_seat = None
                            for rows in selected_theatre.seats:
                                for seats in rows:
                                    if seats in seat:
                                        selected_seat = seat
                                        break
                            if selected_seat is None:
                                print("Invalid Seat selection.")
                            else:
                                for rows in selected_theatre.seats:
                                    for i in range(len(rows)):
                                        if rows[i] in selected_seat:
                                            rows[i] = "0 "
                                total_price = len(selected_seat) * 200
                                print("--------------------------------------------------------\n")
                                print("Booking Preview:")
                                print(f'Movie Details: {selected_movie.movie_name}, {selected_movie.duration}')
                                print(f'Theatre Name: {selected_theatre.theatre_name}')
                                print(f'Show Details: {selected_show.show_time}')
                                print(f'Seat deatisl: {selected_seat}')
                                print(f'Total amount: {total_price}')
                                print("--------------------------------------------------------\n")
                                print("Payment Options:")
                                print("1. Card")
                                print("2. UPI")
                                payment_choice = int(input("Choose a payment option: "))
                                if payment_choice != 1 and payment_choice != 2:
                                    print("Invalid Payment method")
                                else:
                                    if payment_choice == 1:
                                        payment_mode = "Card"
                                        print("Payment Successful")
                                    if payment_choice == 2:
                                        payment_mode = "UPI"
                                        print("Payment Successful")
                                    now=datetime.now()
                                    booked_time=now.strftime("%y/%m/%d, %H:%M:%S")    
                                    booking_details = { "Movie Name": selected_movie.movie_name,
                                                        "Theatre Name": selected_theatre.theatre_name,
                                                        "Show Time": selected_show.show_time,
                                                        "Seats": selected_seat,
                                                        "Total Amount": total_price,
                                                        "Payment Mode": payment_mode,
                                                        "Booked Time": booked_time
                                                      }
                                    self.booking_history.append(booking_details)
                        
            if choice == 2:
                if len(self.booking_history) == 0:
                    print("Booking history is empty.")
                else:
                    print("Booking History:")
                    for booking_history in self.booking_history:
                        print("Movie Name:", booking_history["Movie Name"],"\n"
                              "Theatre Name:", booking_history["Theatre Name"],"\n"
                              "Show Time:", booking_history["Show Time"],"\n"
                              "Seats:", booking_history["Seats"],"\n"
                              "Total Amount:", booking_history["Total Amount"],"\n"
                              "Payment Mode:", booking_history["Payment Mode"],"\n"
                              "Booked Time:", booking_history["Booked Time"],"\n")
            if choice == 3:
                if len(self.booking_history) == 0:
                    print("Booking history is empty.")
                else:
                    del(self.booking_history[-1])
                    print("Your last history has been deleted")
                    choice = input("\n Do you clear your all history? (y/n)")
                    if choice.lower() ==  'y':
                        self.booking_history.clear()
                        print(self.booking_history)
            if choice == 4:
                print("Logout Successfully")
                stay_in_menu = False

class Admins(Users):

    def __init__(self,user_id, user_name, email_id, password, user_role):
        super().__init__(user_id, user_name, email_id, password, user_role)

    def greetings(self):
        print("Welcome Admin!", self.user_name)

        
if __name__ == "__main__":

    app = Users(1, "anand", "anand@gmail.com", "anand123", "user")
    app.hard_code_data()
    app = Users(2, "mohan", "mohan@gmail.com", "mohan123", "admin")
    app.hard_code_data()
    app = Users(3, "hari", "hari@gmail.com", "hari123", "user")
    app.hard_code_data()

    
    login_user = app.validate_user("anand@gmail.com", "anand123")
    if login_user:
        print("Login Success\n")
        
        if login_user.user_role == "user":
            book_ticket = Ticket_booking(login_user.user_id, login_user.user_name, login_user.email_id, login_user.password, login_user.user_role)
            login_user.greetings()
            book_ticket.display_menu()
        elif login_user.user_role == "admin":
            admin = Admins(login_user.user_id, login_user.user_name, login_user.email_id, login_user.password, login_user.user_role)
            admin.greetings()
            
    else:
        print("User does'nt Exist.")
        app.user_id += 1
        user_name = input("Enter the user name")
        email_id = input("Enter your mail_id")
        password = input("Enter a strong password")
        user_role = input("Enter the role")
        app = movie_app(app.user_id, user_name, email_id, password, user_role)
        app.hard_code_data()                    
        
