from tabulate import tabulate
from colorama import Fore, Style, init

# Start Colorama
init(autoreset=True)
#Print a league table for football
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

for i, team in enumerate(teams):

    row = [i + 1, team["Team"], team["Pts"]]

    # League leader in green
    if i == 0:
        row = [
            Fore.GREEN + str(i + 1),
            Fore.GREEN + team["Team"],
            Fore.GREEN + str(team["Pts"])
        ]

    # Bottom two in red
    elif i >= len(teams) - 2:
        row = [
            Fore.RED + str(i + 1),
            Fore.RED + team["Team"],
            Fore.RED + str(team["Pts"])
        ]

    table.append(row)

# Print the league table
print(tabulate(
    table,
    headers=["Pos", "Team", "Points"],
    tablefmt="grid"
))