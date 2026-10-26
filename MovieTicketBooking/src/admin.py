import sqlite3

class Movie:    
    def __init__(self):
      ...

    def add_movie(self,title,genre,show_time,available_seats):
       conn=sqlite3.connect("movie_booking.db")
       cursor=conn.cursor()

       cursor.execute("""
       insert into Movies(title,genre,show_time,available_seats)
       values(?,?,?,?)
       """,(title,genre,show_time,available_seats))
       conn.commit()
       conn.close()

       print(" movie  added succesfully")
      
    def update_movie(self,movie_id,title,genre,show_time,available_seats):
       conn=sqlite3.connect("movie_booking.db")
       cursor=conn.cursor()

       cursor.execute("""
       update Movies
       set title=?,genre=?,show_time=?,available_seats=?
       where movie_id=?
       """,(title,genre,show_time,available_seats,movie_id))
       conn.commit()
       conn.close()

       print("movie updated succesfully") 
        
    def get_all_movie(self):

        conn = sqlite3.connect("movie_booking.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Movies")

        movies = cursor.fetchall()

        if movies:
            for movie in movies:
                print(movie)
        else:
            print("No movies found.")

        conn.close()



    def delete_movie(self, movie_id):

        conn = sqlite3.connect("movie_booking.db")
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM Movies
        WHERE movie_id=?
        """, (movie_id,))

        conn.commit()
        conn.close()

        print("Movie deleted successfully.")

   









