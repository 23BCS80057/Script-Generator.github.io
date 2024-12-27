class GenreExplorer:
    def __init__(self):
        self.genres = {
            "Fantasy": "Once upon a time in a land filled with dragons and magic, there was a hero who...",
            "Science Fiction": "In a future where humanity has colonized distant galaxies, a lone spaceship discovers...",
            "Mystery": "It was a dark and stormy night when Detective Sam arrived at the scene of the crime. The only clue was...",
            "Romance": "On a quiet summer evening, two strangers crossed paths at a charming café, where...",
            "Horror": "Deep in the woods, far from civilization, an abandoned cabin hides secrets that should never be uncovered...",
        }

    def display_genres(self):
        print("Available Genres:")
        for i, genre in enumerate(self.genres.keys(), start=1):
            print(f"{i}. {genre}")

    def get_template(self, choice):
        genre_list = list(self.genres.keys())
        if 1 <= choice <= len(genre_list):
            genre = genre_list[choice - 1]
            print(f"\nGenre: {genre}\nTemplate:\n{self.genres[genre]}")
        else:
            print("Invalid choice. Please select a valid genre.")

    def run(self):
        print("Welcome to the Genre Explorer!")
        while True:
            self.display_genres()
            try:
                choice = int(input("\nChoose a genre by number (or 0 to exit): "))
                if choice == 0:
                    print("Thank you for exploring genres!")
                    break
                self.get_template(choice)
            except ValueError:
                print("Please enter a valid number.")

# Run the Genre Explorer
explorer = GenreExplorer()
explorer.run()
