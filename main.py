loaded_games = []


def show_menu():
    print('----------------MENU-----------------')
    print('1. Wyświetl nazwy wszystkich gier w bazie')
    print('2. Wyświetl wszystkie gry w bazie')
    print('3. Wyświetl TOP 5 gier w bazie')
    print('4. Wyświetl gry z gatunku')
    print('5. Dodaj grę do bazy')
    print('6. Edytuj grę w bazie')
    print('7. Usuń grę z bazy')
    print('8. Wyświetl informację o grze')
    print('9. Oceń grę')
    print('10. Zapisz dane do pliku')
    print('11. Odczytaj dane z pliku')
    print('12. Zakończ')
    print('--------------------------------------')
    operation = input('Wybierz operację jaką chcesz wykonać: ')
    if int(operation) == 1:
        print('Nazwy wszystkich gier')
        list_games_names()
    elif int(operation) == 2:
        print('Wszystkie gry')
        list_all_games()
    elif int(operation) == 3:
        print('TOP 5 gier')
        show_menu()
    elif int(operation) == 4:
        print('Gry z gatunku')
        show_menu()
    elif int(operation) == 5:
        print('Dodaj grę')
        show_menu()
    elif int(operation) == 6:
        print('Edytuj grę')
        show_menu()
    elif int(operation) == 7:
        print('Usuń grę')
        show_menu()
    elif int(operation) == 8:
        print('Info o grze')
        show_menu()
    elif int(operation) == 9:
        print('Oceń grę')
        show_menu()
    elif int(operation) == 10:
        print('Zapisz dane')
        show_menu()
    elif int(operation) == 11:
        print('Odczytaj dane')
        show_menu()
    elif int(operation) == 12:
        print('Kończę działanie programu')
        exit()
    else:
        print('Wybrano błędną operację, spróbuj jeszcze raz!')
        show_menu()


def initialize_database():
    games_data = open('games.txt', 'r')
    games = games_data.readlines()
    for game in games:
        game_info = game.split(',')
        new_game = Game(game_info[0], int(game_info[1]), game_info[2], float(game_info[3].strip()))
        loaded_games.append(new_game)
    games_data.close()


def save_to_database(game_info):
    games_data = open('games.txt', 'a')
    game = game_info
    games_data.writelines(game)


class Game:
    def __init__(self, title, release_year, genre, stats):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.stats = stats


def list_games_names():
    print('Nazwy gier w bazie')
    for index, game in enumerate(loaded_games):
        print(loaded_games[index].title)
    show_menu()


def list_all_games():
    print('Wszystkie gry w bazie')
    for index, game in enumerate(loaded_games):
        print('Gra ', index + 1)
        print('Tytuł: ', loaded_games[index].title)
        print('Rok wydania: ', loaded_games[index].release_year)
        print('Gatunek: ', loaded_games[index].genre)
        print('Ocena graczy: ', loaded_games[index].stats)
    show_menu()


while True:
    initialize_database()
    show_menu()
