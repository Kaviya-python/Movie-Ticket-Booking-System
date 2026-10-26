from src.admin import Movie
from src.user import User
from src.booking import Booking

def main():
    print("="*40)
    print("welcome to movie ticket booking website!!!")
    print("="*40)

    admin_panel=Movie()
    user_panel=User()
    booking_panel=Booking()

    while True:
        print("\n==== Movie ticket booking====\n")
        print("1.Admin Panel")
        print("2.user panel")
        print("3.booking panel")
        print("4.exit")
        print("5.welcome come again!!!")

        choice=input("enter your choice : ")

        if choice=="1":
            while True:
                print("1.Add movie")
                print("2.Update movie")
                print("3.Get all movies")
                print("4.Delete movies")
                print("5.Exit admin panel")
                admin=input("enter your choice : ")

                if admin=="1":
                    title=input("enter the movie title : ")
                    genre=input("enter the movie genre(Action/thriller/comedy/etc) : ")
                    show_time=input("enter the movie timing! : ")
                    available_seats=input("here the available seats!!! : ")
                    admin_panel.add_movie(title,genre,show_time,available_seats)

                elif admin=="2":
                    movie_id=input("Enter Movie ID: ")
                    title=input("enter the new movie title (skip ths block): ")or None
                    genre=input("enter the new movie genre(Action/thriller/comedy/etc) (skip ths block) : ")or None
                    show_time=input("enter the new movie timing! (skip ths block): ")or None
                    available_seats=input("enter availables seats!!! : ")or None
                    admin_panel.update_movie(movie_id,title,genre,show_time,available_seats)

                elif admin=="3":
                    admin_panel.get_all_movie()
                    print("here the movies!!!!")

                elif admin=="4":
                    movie_id=input("enter the movie_id : ")
                    admin_panel.delete_movie(movie_id)

                elif admin=="5":
                    print("Thank you!")
                    break

                else:
                    print("invalid movie choices!!!")

            print("welcome admin panel")

        elif choice=="2":
            while True:
                print("\n==== User Panel ====")
                print("1.Register User")
                print("2.View Users")
                print("3.View Movies")
                print("4.Update User")
                print("5.Delete User")
                print("6.Exit")

                user_choice=input("Enter choice: ")

                if user_choice=="1":
                    name=input("Enter name: ")
                    email=input("Enter email: ")
                    user_panel.add_user(name,email)

                elif user_choice=="2":
                    user_panel.get_all_users()

                elif user_choice=="3":
                    user_panel.view_movies()

                elif user_choice=="4":
                    user_id=input("Enter user id: ")
                    name=input("Enter new name: ")
                    email=input("Enter email: ")
                    user_panel.update_user(user_id,name,email)

                elif user_choice=="5":
                    user_id=input("Enter user id: ")
                    user_panel.delete_user(user_id)

                elif user_choice=="6":
                    break

                else:
                    print("Invalid choice")

            print("welcome to user panel")

        elif choice=="3":
            while True:
                print("\n===== BOOKING PANEL =====")
                print("1. Book Ticket")
                print("2. View My Bookings")
                print("3. Cancel Booking")
                print("4. Back")

                booking_choice=input("Enter your choice: ")

                if booking_choice=="1":
                    booking_panel.book_ticket()

                elif booking_choice=="2":
                    booking_panel.view_user_booking()

                elif booking_choice=="3":
                    booking_panel.cancel_booking()

                elif booking_choice=="4":
                    break

                else:
                    print("Invalid Choice!")

            print("welcome to booking panel")

        elif choice=="4":
            print("thank you !!!")
            break

        elif choice=="5":
            print("welcome come again!")
            break

        else:
            print("invalid choice!!! please enter 1/2/3....")

if __name__=="__main__":
    main()

