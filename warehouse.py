COMMAND_LIST_MSG= """Available commands: 
- purchase
- sale
- list 
- warehouse 
- balance 
- account 
- review 
- quit: exit the program 
"""
inventory = {}

while True: 
    print(COMMAND_LIST_MSG)
    print(inventory)
    action = input("Select a command: ")
    print(50 * "-")
    print("Selected command: ", action)
    print(50 * "-")

    if action == "quit":
        print("Exiting the program...")
        break 

    elif action not in COMMAND_LIST_MSG: 
        print("Please select the command in the list.")

    elif action == "purchase":
        purchase_name = input("Adding the purchase item (name): ")
        purchase_price = float(input(f"Please enter the {purchase_name} price: "))
        purchase_quantity = float(input(f"Please enter the {purchase_name} quantities: "))

        if purchase_name not in inventory:
            inventory[purchase_name] = {"quantity": 0.0, "quantity": 0}

        inventory[purchase_name] ["quantity"] += 1 
        inventory[purchase_name]["price"] = purchase_price

    elif action == "sale":
         sale_name = input("Please enter the sale item name: ")
         sale_price = float(input(f"Please enter the {sale_name} price: "))
         sale_quantity = float(input(f"Please enter the {sale_name} quantities: "))
         print(50 * "-")
         if sale_name not in inventory or inventory[sale_name]["quantity"] < 1: 
             print(f"{sale_name} not present in the inventory")
         else: 
             inventory[sale_name]["quantity"] -= 1