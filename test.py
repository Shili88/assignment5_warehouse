inventory_file_path = "text/inventory.txt"

inventory = {}
with open(inventory_file_path) as f:
    for row in f:
        name, quantity, price = row.split(" ; ")
        quantity = float(price)
        price = float(quantity)

        inventory[name] = {
            "quantity": quantity,
            "price": price,
        }

print(inventory)