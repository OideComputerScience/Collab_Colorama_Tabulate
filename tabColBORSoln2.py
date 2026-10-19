import colorama
from colorama import Fore, Style, init
from tabulate import tabulate

init()

# Dataset: [Item Name, Current Stock]
inventory_items = [
    ["Wireless Mouse", 45],
    ["HDMI Cables", 4],
    ["Mechanical Keyboard", 12],
    ["4K Monitors", 2 ]
]

# Sort by Current Stock in ascending order
# Low stock items will appear first
for i in range(len(inventory_items)):
    for j in range(i + 1, len(inventory_items)):

        if inventory_items[i][1] > inventory_items[j][1]:
            temp = inventory_items[i]
            inventory_items[i] = inventory_items[j]
            inventory_items[j] = temp

# Create table data
table_data = []

for row in inventory_items:

    item = row[0]
    current = row[1]
    min_threshold = 5

    # Evaluate stock levels
    if current < min_threshold:

        stock_styled = (
            Fore.YELLOW
            + str(current)
            + " (LOW STOCK)"
            + Style.RESET_ALL
        )

    else:

        stock_styled = (
            Fore.CYAN
            + str(current)
            + Style.RESET_ALL
        )

    table_data.append([item, stock_styled])

# Table headings
headers = ["Product Item", "Current Stock"]

# Display the table
print(tabulate(
    table_data,
    headers=headers,
    tablefmt="presto",
    numalign="center"
))