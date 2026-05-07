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
            users_data.remove(user)


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

