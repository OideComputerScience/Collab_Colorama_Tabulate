''' This example demonstrates the use of colorama in changing
the colour of text and the background. It also demonstrates how
style can be changed. '''

import colorama
from colorama import Fore, Back, Style, init

#it is good practice to initialise colorama 
init()

#colorama can be simply used to change the colour of text.
print(Fore.RED + "This text is red. ")
print(Fore.GREEN + "This text is green. ")

#Note here that the text remains green
print("Hello")

#To reset the text back to normal stings reset it.
print(Style.RESET_ALL + "Back to normal text");

#We can also change the background colour
print(Back.GREEN + "This text has a green background. ")
print(Style.BRIGHT + "This text is bright.")

#Reset
print(Style.RESET_ALL + "Back to normal text");
#we can combine text with different colours and styles.
print(Style.DIM + Fore.YELLOW + Back.CYAN + 'Dim yellow text on cyan background')

