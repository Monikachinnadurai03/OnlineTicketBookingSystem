from datetime import datetime

class Movie:
    def __init__(self, title, duration, director, rating):
        self.title = title
        self.duration = duration
        self.director = director
        self.rating = rating
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def get_reviews(self):
        return self.reviews

class Theater:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.movies = []
        self.showtimes = {}

    def add_movie(self, movie, showtimes):
        self.movies.append(movie)
        self.showtimes[movie.title] = showtimes

    def get_movies(self):
        return self.movies

    def get_showtimes(self, movie_title):
        return self.showtimes.get(movie_title, [])

class Seat:
    def __init__(self, seat_number, is_booked=False):
        self.seat_number = seat_number
        self.is_booked = is_booked

    def book_seat(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        else:
            return False

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.booking_history = []

    def add_booking_history(self, booking):
        self.booking_history.append(booking)

    def get_booking_history(self):
        return self.booking_history

class Booking:
    def __init__(self, user, movie, theater, showtime, seat_number):
        self.user = user
        self.movie = movie
        self.theater = theater
        self.showtime = showtime
        self.seat_number = seat_number
        self.booking_time = datetime.now()

class BookingSystem:
    def __init__(self):
        self.theaters = []
        self.users = []

    def add_theater(self, theater):
        self.theaters.append(theater)

    def get_theaters(self):
        return self.theaters

    def register_user(self, username, password):
        user = User(username, password)
        self.users.append(user)
        print("User registered successfully!")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                print("Login successful!")
                return user
        print("Invalid credentials. Please try again.")
        return None

    def book_ticket(self, user, theater_name, movie_title, showtime, seat_number):
        theater = None
        movie = None

        # Find the theater
        for t in self.theaters:
            if t.name == theater_name:
                theater = t
                break

        if theater is None:
            print("Theater not found.")
            return

        # Find the movie in the theater
        for m in theater.get_movies():
            if m.title == movie_title:
                movie = m
                break

        if movie is None:
            print("Movie not found in the theater.")
            return

        # Find the seat in the theater
        for seat in theater.get_showtimes(movie.title)[showtime]:
            if seat.seat_number == seat_number:
                if not seat.book_seat():
                    print("Seat already booked.")
                    return
                break
        else:
            print("Invalid seat number.")
            return

        booking = Booking(user, movie, theater, showtime, seat_number)
        user.add_booking_history(booking)
        print("Ticket booked successfully!")
        print("Movie:", movie.title)
        print("Theater:", theater.name)
        print("Showtime:", showtime)
        print("Seat Number:", seat_number)

    def rate_movie(self, user, movie_title, rating):
        for theater in self.theaters:
            for movie in theater.get_movies():
                if movie.title == movie_title:
                    movie.rating = rating
                    print("Movie rating updated successfully!")
                    return

        print("Movie not found.")

    def add_review(self, user, movie_title, review):
        for theater in self.theaters:
            for movie in theater.get_movies():
                if movie.title == movie_title:
                    movie.add_review(review)
                    print("Review added successfully!")
                    return

        print("Movie not found.")


# Example Usage
if __name__ == "__main__":
    # Creating movies
    movie1 = Movie("Movie 1", 120, "Director 1", "PG")
    movie2 = Movie("Movie 2", 150, "Director 2", "R")

    # Creating theaters
    theater1 = Theater("Theater 1", "Location 1")
    theater2 = Theater("Theater 2", "Location 2")

    # Adding movies to theaters
    theater1.add_movie(movie1, {"10:00 AM": [Seat("A1"), Seat("A2"), Seat("A3")],
                               "2:00 PM": [Seat("B1"), Seat("B2"), Seat("B3")],
                               "6:00 PM": [Seat("C1"), Seat("C2"), Seat("C3")]})

    theater2.add_movie(movie2, {"11:00 AM": [Seat("A1"), Seat("A2"), Seat("A3")],
                               "3:00 PM": [Seat("B1"), Seat("B2"), Seat("B3")],
                               "7:00 PM": [Seat("C1"), Seat("C2"), Seat("C3")]})


    # Creating booking system
    booking_system = BookingSystem()

    # Adding theaters to the booking system
    booking_system.add_theater(theater1)
    booking_system.add_theater(theater2)

    # Registering users
    booking_system.register_user("user1", "password1")
    booking_system.register_user("user2", "password2")

    # Logging in
    user = booking_system.login("user1", "password1")

    if user:
        # Booking a ticket
        booking_system.book_ticket(user, "Theater 1", "Movie 1", "10:00 AM", "A1")

        # Rating a movie
        booking_system.rate_movie(user, "Movie 1", "5 stars")

        # Adding a review
        booking_system.add_review(user, "Movie 1", "Great movie!")
