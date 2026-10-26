import sqlite3


class Booking:

    def __init__(self):
        pass

    def book_ticket(self):

        conn = sqlite3.connect("movie_booking.db")
        cursor = conn.cursor()

        email = input("Enter your Email: ")

        cursor.execute("""
        SELECT user_id, name
        FROM Users
        WHERE email = ?
        """, (email,))

        user = cursor.fetchone()

        if user is None:
            print("User not found. Please register first!")
            conn.close()
            return

        print(f"\nWelcome {user[1]}")

        cursor.execute("""
        SELECT movie_id, title, genre, show_time, available_seats
        FROM Movies
        """)

        movies = cursor.fetchall()

        if not movies:
            print("No movies available.")
            conn.close()
            return

        print("\n========== Available Movies ==========")

        for movie in movies:
            print(f"""
Movie ID : {movie[0]}
Title    : {movie[1]}
Genre    : {movie[2]}
Show Time: {movie[3]}
Seats    : {movie[4]}
---------------------------------------
""")

        movie_id = int(input("Enter Movie ID : "))
        seats = int(input("Enter Number of Seats : "))

        cursor.execute("""
        SELECT available_seats
        FROM Movies
        WHERE movie_id = ?
        """, (movie_id,))

        result = cursor.fetchone()

        if result is None:
            print("Invalid Movie ID")
            conn.close()
            return

        available_seats = result[0]

        if seats > available_seats:
            print("Sorry! Not enough seats available.")
            conn.close()
            return

        cursor.execute("""
        INSERT INTO Bookings(user_id, movie_id, seats_booked)
        VALUES (?, ?, ?)
        """, (user[0], movie_id, seats))

        cursor.execute("""
        UPDATE Movies
        SET available_seats = available_seats - ?
        WHERE movie_id = ?
        """, (seats, movie_id))

        conn.commit()
        conn.close()

        print("\nTicket Booked Successfully!")

    def view_user_booking(self):

        conn = sqlite3.connect("movie_booking.db")
        cursor = conn.cursor()

        email = input("Enter your Email: ")

        cursor.execute("""
        SELECT user_id
        FROM Users
        WHERE email = ?
        """, (email,))

        user = cursor.fetchone()

        if user is None:
            print("User not found!")
            conn.close()
            return

        cursor.execute("""
        SELECT
            b.booking_id,
            m.title,
            m.genre,
            m.show_time,
            b.seats_booked
        FROM Bookings b
        JOIN Movies m
        ON b.movie_id = m.movie_id
        WHERE b.user_id = ?
        """, (user[0],))

        bookings = cursor.fetchall()

        if not bookings:
            print("No Bookings Found.")
        else:
            print("\n===== My Bookings =====")

            for booking in bookings:
                print(f"""
Booking ID : {booking[0]}
Movie      : {booking[1]}
Genre      : {booking[2]}
Show Time  : {booking[3]}
Seats      : {booking[4]}
----------------------------
""")

        conn.close()

    def cancel_booking(self):

        conn = sqlite3.connect("movie_booking.db")
        cursor = conn.cursor()

        booking_id = int(input("Enter Booking ID to Cancel: "))

        cursor.execute("""
        SELECT movie_id, seats_booked
        FROM Bookings
        WHERE booking_id = ?
        """, (booking_id,))

        booking = cursor.fetchone()

        if booking is None:
            print("Invalid Booking ID")
            conn.close()
            return

        movie_id = booking[0]
        seats = booking[1]

        cursor.execute("""
        DELETE FROM Bookings
        WHERE booking_id = ?
        """, (booking_id,))

        cursor.execute("""
        UPDATE Movies
        SET available_seats = available_seats + ?
        WHERE movie_id = ?
        """, (seats, movie_id))

        conn.commit()
        conn.close()

        print("Booking Cancelled Successfully!")