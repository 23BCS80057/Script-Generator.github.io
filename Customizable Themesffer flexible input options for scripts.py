import json

# Define default themes
themes = {
    "light": {
        "background": "#ffffff",
        "text": "#000000",
        "highlight": "#cccccc",
    },
    "dark": {
        "background": "#000000",
        "text": "#ffffff",
        "highlight": "#444444",
    },
}

def load_theme(theme_name):
    """
    Loads a predefined theme or allows user to customize it.
    """
    if theme_name in themes:
        print(f"Loaded {theme_name} theme.")
        return themes[theme_name]
    else:
        print("Theme not found. Creating a new custom theme...")
        return create_custom_theme()

def create_custom_theme():
    """
    Allows the user to define a custom theme.
    """
    print("Define your custom theme (leave blank for default values):")
    background = input("Background color (e.g., #ffffff): ") or "#f0f0f0"
    text = input("Text color (e.g., #000000): ") or "#000000"
    highlight = input("Highlight color (e.g., #cccccc): ") or "#ffcc00"
    return {
        "background": background,
        "text": text,
        "highlight": highlight,
    }

def save_theme(theme, file_name="custom_theme.json"):
    """
    Saves the theme configuration to a file.
    """
    with open(file_name, "w") as file:
        json.dump(theme, file, indent=4)
    print(f"Theme saved to {file_name}.")

def apply_theme(theme):
    """
    Applies the selected theme (mock application).
    """
    print("\nApplying theme...")
    print(f"Background color: {theme['background']}")
    print(f"Text color: {theme['text']}")
    print(f"Highlight color: {theme['highlight']}")
    print("Theme applied successfully!\n")

# Main script
print("Available themes: light, dark")
selected_theme = input("Choose a theme: ").strip().lower()
theme = load_theme(selected_theme)
apply_theme(theme)

if input("Do you want to save this theme? (yes/no): ").strip().lower() == "yes":
    save_theme(theme)
