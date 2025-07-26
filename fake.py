import random

# --- 1. Lists of words ---
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai local train",
    "a plate of samosa",
    "inside Parliament",
    "at Ganga Ghat",
    "during IPL match",
    "at India Gate"
]

# --- 2. Headline generator loop ---
while True:
    # Pick one random item from each list
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    # Build the headline
    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}!"
    print("\n" + headline)  # Print it
    
    # Ask the user if they want another
    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        print("\nThanks for using the Fake News Headline Generator. Have a nice day!")
        break
