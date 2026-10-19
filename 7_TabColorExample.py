from tabulate import tabulate
from colorama import Fore, Style, init

# Start Colorama
init()
#Print a league table for football
#This makes use of a dictionary
teams = [
    {"Team": "Liverpool", "Pts": 82},
    {"Team": "Arsenal", "Pts": 78},
    {"Team": "Chelsea", "Pts": 65},
    {"Team": "Brighton", "Pts": 52},
    {"Team": "Burnley", "Pts": 24},
    {"Team": "Sheffield Utd", "Pts": 18}
]

# Basic sorting using a loop
# Compare each team's points and swap them if necessary

for i in range(len(teams)):
    for j in range(i + 1, len(teams)):

        if teams[i]["Pts"] < teams[j]["Pts"]:
            temp = teams[i]
            teams[i] = teams[j]
            teams[j] = temp

# Create the table
table = []
#enumerate keeps track of the index and the value
for i, team in enumerate(teams):

    row = [i + 1, team["Team"], team["Pts"]]

    # League leader in blue
    if i == 0:
        row = [
            Fore.BLUE + str(i + 1),
            Fore.BLUE + team["Team"],
            Fore.BLUE + str(team["Pts"])
        ]

    # Bottom two in Yellow
    elif i >= len(teams) - 2:
        row = [
            Fore.YELLOW + str(i + 1),
            Fore.YELLOW + team["Team"],
            Fore.YELLOW + str(team["Pts"])
        ]

    table.append(row)

# Print the league table
print(tabulate(
    table,
    headers=["Pos", "Team", "Points"],
    tablefmt="grid"
))