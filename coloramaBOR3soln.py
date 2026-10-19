import colorama
from colorama import Fore, init

# Initialise Colorama
init()

# Ask the user for input
message_type = input("Enter error, warning, or info: ").strip().lower()

# Display a coloured output
if message_type == "error":
    print(Fore.RED + "ERROR: Something went wrong!")

elif message_type == "warning":
    print(Fore.YELLOW + "WARNING: Please be careful!")

elif message_type == "info":
    print(Fore.GREEN + "INFO: Everything is working correctly.")

else:
    print(Fore.WHITE + "Invalid input. Please enter error, warning, or info.")
