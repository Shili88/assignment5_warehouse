# save and loading (3 functions for each) - balance, inventory (apple;10;5 - each row represent 1 product), operation history (history = keep the sentence - does not have to be translate to anything - review at the warehouse)
def load_inventory(inventory_file_path="text/inventory.txt"):
    inventory = {}
    with open(inventory_file_path) as f:
        for row in f:
            name, price, quantity = row.strip().split(";")
            price = float(price)
            quantity =float(quantity)

            if name in inventory:
                print(f"Warning: duplicate value of {name}") 
            
            inventory[name] = {
                "price": price,
                "quantity": quantity,
            }
    return inventory

inventory = load_inventory("text/inventory.txt")
print(inventory)