import colorama
from colorama import Fore, Style, init
from tabulate import tabulate

init()

# Dataset: [Name, Score]
students = [
    ["Alice", 85],
    ["Bob", 42],
    ["Charlie", 91],
    ["David", 58],
    ["Emily", 73]
]

# Sort students by score in descending order
for i in range(len(students)):
    for j in range(i + 1, len(students)):

        if students[i][1] < students[j][1]:
            temp = students[i]
            students[i] = students[j]
            students[j] = temp
            
table_data = []
 # Evaluate performance
for row in students:

    name = row[0]
    score = row[1]

    # Evaluate performance
    if score >= 60:
        status = "PASSED"

        score_str = (
            Fore.BLUE
            + str(score)
            + Style.RESET_ALL
        )

        status_str = (
            Fore.BLUE
            + status
            + Style.RESET_ALL
        )

    else:
        status = "FAILED"

        score_str = (
            Fore.MAGENTA
            + str(score)
            + Style.RESET_ALL
        )

        status_str = (
            Fore.MAGENTA
            + status
            + Style.RESET_ALL
        )

    table_data.append([name, score_str, status_str])

headers = ["Student Name", "Exam Score", "Status"]
print(tabulate(table_data, headers=headers, tablefmt="rounded_grid"))