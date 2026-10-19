import colorama
from colorama import Fore, Style, init

# Initialise Colorama
init()

# Ask the user for their mood
mood = input("How are you feeling today? ").strip().lower()

# Display a coloured message based on the mood
if mood == "happy":
    print(Fore.GREEN + "That's great! Keep smiling! ")
elif mood == "sad":
    print(Fore.BLUE + "I'm sorry you're feeling sad. Things can get better. ")
elif mood == "angry":
    print(Fore.RED + "Take a deep breath and try to relax. ️")
elif mood == "excited":
    print(Fore.YELLOW + "Fantastic! Enjoy your excitement! ")
elif mood == "tired":
    print(Fore.MAGENTA + "You deserve some rest. Take it easy!")
else:
    print(Fore.WHITE + "Thanks for sharing your mood! ")
