import random


def get_inspiration():
    prompts = [
        "Write a scene where the main character finds an unexpected letter.",
        "Describe a place you've never been but would like to visit.",
        "Write about a day in the life of a character who has no memory of their past.",
        "Create a story that starts with: 'It was a quiet evening until the knock on the door.'",
        "Imagine a world where everyone can read each other's thoughts. How does it change society?"
    ]
    
    exercises = [
        "Write for 10 minutes without stopping. Let the words flow freely without editing.",
        "Pick a random word from the dictionary and write a paragraph using it as inspiration.",
        "Use a photo or painting to create a backstory for the person in the image.",
        "Describe an object you use daily, but write about it from the perspective of the object itself.",
        "Write a letter to your future self about your hopes and dreams."
    ]
    
    tips = [
        "Don't worry about perfection, just write. Editing comes later.",
        "Take a break and go for a walk. Inspiration often strikes when you step away.",
        "Try changing your environment—move to a different room, a café, or even outside.",
        "Read something outside your genre. New ideas often come from unexpected places.",
        "Set a timer for 20 minutes and write as much as you can in that time. It’s better to have something than nothing."
    ]
    
    # Randomly select an item from each category
    prompt = random.choice(prompts)
    exercise = random.choice(exercises)
    tip = random.choice(tips)
    
    # Display the inspiration
    print("Inspiration Boost:\n")
    print("Writing Prompt: " + prompt)
    print("\nWriting Exercise: " + exercise)
    print("\nTip for Overcoming Writer's Block: " + tip)

# Call the function to get inspiration
get_inspiration()
