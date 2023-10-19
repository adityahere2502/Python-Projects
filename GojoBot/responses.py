import random

def handle_response(user_message):
    greetings = [
        "Yo, what's up?",
        "Hello there, my dear friend.",
        "Hey, kiddo!",
        "Good to see you again!",
    ]
    special_moves = [
        "Get ready for a taste of my Limitless Cursed Technique!",
        "Let's unleash the Six Eyes and get this party started!",
        "How about some Cursed Energy in action?",
    ]
    questions = [
        "What's on your mind?",
        "Ask your question, and I'll give you the answer.",
        "You've got a burning question, don't you?",
        "Curiosity is a good thing! What do you want to know?",
    ]
    compliments = [
        "You're as clever as always!",
        "Good question, you're on the right track.",
        "You're pretty smart, huh?",
        "You have a sharp mind!",
    ]
    casual_responses = [
        "Interesting...",
        "I see...",
        "Tell me more.",
        "Keep it coming, kiddo.",
        "Let's chat about it.",
        "Curious about something else?",
    ]
    goodbyes = [
        "Ahhh See you later",
        "You tired take rest",
        "Bye Bye",
        "Ora make sure you say me bye too.",
        "GoodBye",
        "Okey Bye.",
    ]

    user_message = user_message.lower()

    if any(word in user_message for word in ["hi", "hello", "hey"]):
        return random.choice(greetings)
    elif any(word in user_message for word in ["special move", "cursed technique"]):
        return random.choice(special_moves)
    elif any(word in user_message for word in ["how are you", "are you okay"]):
        return "I'm feeling Limitless, as always. How about you?"
    elif "?" in user_message:
        return random.choice(questions)
    elif any(word in user_message for word in ["you're the best", "you're amazing"]):
        return random.choice(compliments)
    elif any(word in user_message for word in ["goodbye", "bye","i'm tired bye", "i want to sleep"]):
        return random.choice(goodbyes)
    else:
        return random.choice(casual_responses)
