import colorama
from colorama import Fore, Style, init

# Initialise Colorama
init()

# Ask the user for an instruction
instruction = input("Enter Go, Wait, or Stop: ").strip().lower()

# Display the message in colour
if instruction == "go":
    print(Fore.GREEN + "GO! You may proceed.")
elif instruction == "wait":
    print(Fore.YELLOW + "WAIT! Please be patient.")
elif instruction == "stop":
    print(Fore.RED + "STOP! Do not proceed.")
else:
    print(Fore.WHITE + "Invalid input. Please enter Go, Wait, or Stop.")
