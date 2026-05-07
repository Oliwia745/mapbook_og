from mapbook_lb.model import users

from mapbook_lb.controler import read_users, adder_users, remove_users, update_users, update_users_post

def main():

    while True:
        print("=====MENU======")
        print("0 - zakończ program")
        print("1 - Wyświetl znajomych")
        print("2 - Dodanie znajomego")
        print("3 - Usuwanie znajomego")
        print("4 - Update znajomego")
        print("5 - Update postów")


        choice=input("Wybierz opcje menu: ")
        print(f"Wybrono opcję {choice}")
        if choice == "0":
            break

        if choice == "1":
            read_users(users)

        if  choice == "2":
            add_users(users)

        if choice == "3":
            remove_users(users)

        if choice == "4":
            remove_users(users)

        if choice == "5":
            remove_users(users)
if __name__ == "__main__":
    main()