inventory = {"Apples": 150, "Bananas": 225, "Cherries": 75}
price = 2.50
inventory_value = 0
for stock in inventory.values():
    total = price*stock
    inventory_value += total
print(f"${inventory_value:.2f}")
