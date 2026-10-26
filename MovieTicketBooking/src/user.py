import sqlite3

class User:

    def __init__(self):
        ...


    def add_user(self, name, email):
        conn = sqlite3.connect("movie_booking.db")
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Users(name, email)
        VALUES(?,?)
        """,(name,email))

        conn.commit()
        conn.close()

        print("User registered successfully")


    def get_all_users(self):
        conn = sqlite3.connect("movie_booking.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users")
        users = cursor.fetchall()

        if users:
            for user in users:
                print(user)
        else:
            print("No users found")

        conn.close()


    def update_user(self,user_id,name,email):
        conn = sqlite3.connect("movie_booking.db")
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE Users
        SET name=?, email=?
        WHERE user_id=?
        """,(name,email,user_id))

        conn.commit()
        conn.close()

        print("User updated successfully")
        
    def view_movies(self):
        conn = sqlite3.connect("movie_booking.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Movies")
        movies = cursor.fetchall()

        if movies:
            for movie in movies:
                print(movie)
        else:
            print("No movies found")

        conn.close()    


    def delete_user(self,user_id):
        conn = sqlite3.connect("movie_booking.db")
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM Users
        WHERE user_id=?
        """,(user_id,))

        conn.commit()
        conn.close()

        print("User deleted successfully")



