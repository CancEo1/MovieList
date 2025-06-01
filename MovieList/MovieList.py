# Program to add, delete, and view movies in a list.
# 
def display_menu():
    print("Movie List Menu:")
    print("list - List all movies")
    print("add - Add a movie")
    print("remove - Remove a movie")
    print("exit - Exit the program")
    print()

def list_movies(movie_list):
    for movie in movie_list:
        for item in movie:
            print(item, end=" | ")
        print()

def add_movie(movie_list):
    movie = input("Name: ")
    movie_list.append(movie)
    print(f"{movie} was added.\n")

def remove_movie(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid number.\n")
    else:
        movie = movie_list.pop(number - 1)
        print(f"{movie} was removed.\n")

def main():
    movie_list = [["The Shawshank Redemption", 1982, 10],
        ["The Godfather", 1972, 10],
        ["The Dark Knight", 2008, 9.5],
        ["Pulp Fiction", 1994, 8],
        ["Forrest Gump", 1994, 10]]

    display_menu()

    while True:
        command = input("Command:")
        if command.lower() == "list":
            list_movies(movie_list)
        elif command.lower() == "add":
            add_movie(movie_list)
        elif command.lower() == "remove":
            remove_movie(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please Try again.\n")
    print("Goodbye!")

if __name__ == "__main__":
    main()