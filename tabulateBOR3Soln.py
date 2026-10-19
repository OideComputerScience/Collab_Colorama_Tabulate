from tabulate import tabulate

employees = [
    ["Liam O'Connor", "Sales"],
    ["Emma Murphy", "Marketing"],
    ["Sean Walsh", "Engineering"]
]
headers = ["Employee", "Department"]

# stralign controls text columns, numalign controls numeric columns
print(tabulate(
    employees, 
    headers=headers, 
    tablefmt="pipe", 
    stralign="left", 
    showindex="always"
))