# Program to add, delete, and view movies in a list.
# 
def display_menu():
    print("Movie List Menu:")
    print("list - List all movies")
    print("add - Add a movie")
    print("remove - Remove a movie")
    print("exit - Exit the program")
    print()

# Make a list of the movies with multi-dimensional array
def list_movies(movie_list):
    if len(movie_list) == 0:
        print("No movies in the list.\n")
    else:
        for i, movie in enumerate(movie_list, start=1):
            print(f"{i}. {movie[0]} ({movie[1]})")
        print()

# Function to add a movie
def add_movie(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    movie = [name, year]
    movie_list.append(movie)
    print(f"{movie} was added.\n")
# Remove movie
def remove_movie(movie_list):
    number = int(input("Number: "))
    # Check if the number is valid
    if number < 1 or number > len(movie_list):
        print("Invalid number.\n")
    # If number is valid and in range, remove the movie
    else:
        movie = movie_list.pop(number - 1)
        print(f"{movie} was removed.\n")
# Main function to run the program
def main():
    movie_list = [["The Shawshank Redemption", 1982, 10],
        ["The Godfather", 1972, 10],
        ["The Dark Knight", 2008, 9.5],
        ["Pulp Fiction", 1994, 8],
        ["Forrest Gump", 1994, 10]]
    # Display rules and menu
    display_menu()
    # Main loop to handle commands
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
# Call the main method to the IDE and run program
if __name__ == "__main__":
    main()