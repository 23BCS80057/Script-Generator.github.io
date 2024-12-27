import openai

# Set up your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def generate_script(genre, characters, plot):
    """
    Generates a movie script based on user inputs.

    Args:
        genre (str): The genre of the movie.
        characters (list of str): Names and brief descriptions of characters.
        plot (str): A brief plot outline.

    Returns:
        str: Generated movie script.
    """
    prompt = (
        f"Write a movie script in the {genre} genre.\n\n"
        f"Characters: {', '.join(characters)}\n\n"
        f"Plot: {plot}\n\n"
        f"Script:\n"
    )

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use a GPT-3.5/4 engine
            prompt=prompt,
            max_tokens=1000,
            temperature=0.7
        )
        script = response.choices[0].text.strip()
        return script
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("Welcome to the Automated Scriptwriting Tool!\n")

    # Gather user inputs
    genre = input("Enter the genre of the movie (e.g., action, comedy, drama): ")
    num_characters = int(input("How many main characters are there? "))

    characters = []
    for i in range(num_characters):
        character = input(f"Enter a brief description of character {i + 1} (e.g., John, a brave firefighter): ")
        characters.append(character)

    plot = input("Describe the basic plot of the movie: ")

    print("\nGenerating your movie script...\n")

    # Generate the script
    script = generate_script(genre, characters, plot)

    print("\nHere is your generated script:\n")
    print(script)
