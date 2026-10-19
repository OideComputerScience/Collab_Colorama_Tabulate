import colorama
from colorama import Fore, Style
from tabulate import tabulate

# Initialize Colorama
colorama.init(autoreset=True)

# Dataset: [Employee Name, Quarterly Sales Amount]
sales_data = [
    ["Michael Scott", 32000],
    ["Dwight Schrute", 68500],
    ["Jim Halpert", 54000],
    ["Ryan Howard", 12000],
    ["Phyllis Vance", 51500]
]

# Sort by Quarterly Sales in descending order
# Highest sales will appear first
for i in range(len(sales_data)):
    for j in range(i + 1, len(sales_data)):

        if sales_data[i][1] < sales_data[j][1]:
            temp = sales_data[i]
            sales_data[i] = sales_data[j]
            sales_data[j] = temp

# Create table data
table_data = []

for row in sales_data:

    name = row[0]
    sales = row[1]

    # Format sales as currency
    formatted_sales = "€%.2f" % sales

    # Check if target milestone was reached
    if sales >= 50000:

        # Green if sales are 50,000 or more
        sales_str = "%s%s%s" % (
            Fore.GREEN,
            formatted_sales,
            Style.RESET_ALL
        )

    else:

        # Red if sales are below 50,000
        sales_str = "%s%s%s" % (
            Fore.RED,
            formatted_sales,
            Style.RESET_ALL
        )

    table_data.append([name, sales_str])

# Table headings
headers = ["Employee Name", "Q3 Total Sales"]

# Display the table
print(tabulate(
    table_data,
    headers=headers,
    tablefmt="fancy_grid"
))