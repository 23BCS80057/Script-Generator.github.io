import datetime


def generate_script(topic, purpose, audience):
    """
    Generate a basic script outline for a given topic.
    
    Args:
        topic (str): The main topic of the script.
        purpose (str): The purpose of the script (e.g., educate, entertain, inform).
        audience (str): The target audience of the script.

    Returns:
        str: A formatted script outline.
    """
    script_outline = f"""
    Script Title: {topic.capitalize()}
    Date: {datetime.datetime.now().strftime('%Y-%m-%d')}

    Purpose: {purpose.capitalize()}
    Target Audience: {audience.capitalize()}

    Outline:
    1. Introduction
    - Greet the audience
    - Briefly introduce the topic: "{topic}"

    2. Main Content
    - Key point 1 about {topic}
    - Key point 2 about {topic}
    - Key point 3 about {topic}

    3. Conclusion
    - Summarize the main points
    - Thank the audience
    - Call-to-action (if applicable)
    """
    return script_outline.strip()

# Example usage
topic = "Time Management"
purpose = "educate"
audience = "students"

script = generate_script(topic, purpose, audience)
print(script)
