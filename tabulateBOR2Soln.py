from tabulate import tabulate

# --- Solution 1 ---
print("--- Breakout Room Group 2 ---")
data = [["Laptops", 1999.99], ["Mouse", 12.55], ["Monitor", 150]]
headers = ["Product", "Price (€)"]
#print(tabulate(data, headers=headers))

print(tabulate(data, headers=headers, numalign="left", stralign = "center", tablefmt="outline"))