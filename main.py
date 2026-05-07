# definicja prostejn struktury danych obejmującej przykładowego użytkownika

users = [
    {"name": "Oliwia", "Location": "Uciekajka", "posts": ["Sprzedam mercedesa", "Kupe skrzynie biegow",
                                                          "Ratunku co robic po wypadku", "Kto dziaisj idzie biegac?"]},
    {"name": "Alicja", "Location": "Bugzy Ploskie", "posts": ["Moj kod nie dziala pomocy!"]},
    {"name": "Patrycja", "Location": "Krasnosiedl", "posts": ["Czy ktos zrobil sprawozdanie z PPyth?"]},

]


def read_users(users_data: list) -> None:
    for user in users_data:
        print(f"Twoj znajomy {user['name']} z miejscowosci {user['Location']} opublikował {user['posts'][-1]}")


def adder_users(users_data: list) -> None:
    users_data.append({"name": input("Podaj imie uzytkownika:"), "Location": input("Podaj swoja lokalizacje:"),
                       "posts": ["Dolaczono do znajomych"]})



def remove_users(users_data: list) -> None:
    user_to_remove = input("Podaj imie znajomego do usunięcia:")
    for user in users_data:
        if user["name"] == user_to_remove:
            users.remove(user)


def update_users(users_data: list) -> None:
    user_to_update = input("Podaj imie znajomego do update:")
    for user in users_data:
        if user["name"] == user_to_update:
            user["name"]= input("Podaj nowe imie uzytkownika:")
            user["name"]= input("Podaj nowa lokalizacje:")

def update_users_post(users_data: list) -> None:
    user_to_update = input("Podaj imie znajomego do update:")
    for user in users_data:
        if user["name"] == user_to_update:
            user["post"]= input("Co słychać:")






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
