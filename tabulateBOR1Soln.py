from tabulate import tabulate

# --- Solution 1 ---
print("--- Breakout Room Group 1 ---")
data = [["Apple", 12, 0.50], ["Banana", 50, 0.20], ["Cherry", 30, 1.50]]
headers = ["Item", "Quantity", "Price (€)"]
#print(tabulate(data, headers=headers))

print(tabulate(data, headers=headers, numalign="right", tablefmt="fancy_grid"))