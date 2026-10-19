'''This example creates a simple progress bar that updates
in the terminal. The style is bright, colour is blue.
The time modules also needs to be imported. '''

import time
import colorama
from colorama import Fore, Back, Style, init

init() #it is good practice to initialise colorama

#create a progress bar from 0-100%
for i in range(101):
    print(Style.BRIGHT + Fore.BLUE + "\rProgress: {}%".format(i), end="") 
    #print(Style.BRIGHT + Fore.BLUE + f"\rProgress: {i}%", end="") #using f string
    time.sleep(0.1)