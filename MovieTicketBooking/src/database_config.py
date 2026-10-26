
import sqlite3

conn = sqlite3.connect("movie_booking.db")
cursor = conn.cursor()


CREATE_MOVIES_TABLE="""
CREATE TABLE IF NOT EXISTS Movies (
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT,
    show_time TEXT NOT NULL,
    available_seats INTEGER NOT NULL
);
"""

CREATE_USERS_TABLE="""
CREATE TABLE  IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
"""
CREATE_BOOKINGS_TABLE="""
CREATE TABLE IF NOT EXISTS Bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    seats_booked INTEGER NOT NULL,
    booking_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
);
"""

cursor.execute(CREATE_MOVIES_TABLE)
cursor.execute(CREATE_USERS_TABLE)
cursor.execute(CREATE_BOOKINGS_TABLE)




print("Database Connected")
