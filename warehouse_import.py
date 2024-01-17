import os 

# Inventory Load
def load_inventory(user, inventory_file_path_tmpl="text/inventory_{}.txt"):
    inventory_file_path = inventory_file_path_tmpl.format(user)
    inventory = {}
    if not os.path.exists(inventory_file_path):
        return inventory
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

# Inventory Save 
def save_inventory(inventory, user, inventory_file_path_tmpl="text/inventory_{}.txt"):
    inventory_file_path = inventory_file_path_tmpl.format(user)
    with open(inventory_file_path, "w") as f:
        for product_name, stats in inventory.items():
            f.write("{};{};{}\n".format(product_name, stats["price"], stats["quantity"]))

# Load history
def load_history(user, history_file_path_tmpl="text/history_{}.txt"):
    history_file_path = history_file_path_tmpl.format(user)
    history = []
    if not os.path.exists(history_file_path):
        return history
    with open(history_file_path) as f:
        for row in f:
            history.append(row.strip())
    return history 

# save history
def save_history(history, user, history_file_path_tmpl="text/history_{}.txt"):
    history_file_path = history_file_path_tmpl.format(user)
    with open(history_file_path, "w") as f:
        for row in history:
            f.write(f"{row}\n")

# balance load 
def load_balance(user, balance_file_path_tmpl="text/balance_{}.txt"):
    balance_file_path = balance_file_path_tmpl.format(user)
    balance = {}
    if not os.path.exists(balance_file_path):
        return balance
    with open(balance_file_path) as f:
        for row in f:
            balance_command, amount = row.strip().split(";")
            amount = str(amount)

            if balance_command in balance:
                print(f"Warning: duplicate value of {name}") 
            
            balance[balance_command] = {
                "amount": amount,
            }
    return balance


# balance Save 
def save_balance(balance, user, balance_file_path_tmpl="text/balance_{}.txt"):
    balance_file_path = balance_file_path_tmpl.format(user)
    with open(balance_file_path, "w") as f:
        for balance_command, stats in balance.items():
            f.write("{};{}\n".format(balance_command, stats["amount"]))