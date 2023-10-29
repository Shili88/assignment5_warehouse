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
        print(50 * "-")

    elif action == "purchase":
        purchase_name = input("Adding the purchase item (name): ")
        purchase_price = float(input(f"Please enter the {purchase_name} price: "))
        purchase_quantity = float(input(f"Please enter the {purchase_name} quantities: "))

        if purchase_name not in inventory:
            inventory[purchase_name] = {"quantity": 0.0, "quantity": 0}

        inventory[purchase_name] ["quantity"] += purchase_quantity
        inventory[purchase_name]["price"] = purchase_price

    elif action == "sale":
         sale_name = input("Please enter the sale item name: ")
         sale_price = float(input(f"Please enter the {sale_name} price: "))
         sale_quantity = float(input(f"Please enter the {sale_name} quantities: "))
         print(50 * "-")
         if sale_name not in inventory or inventory[sale_name]["quantity"] < 1: 
             print(f"{sale_name} not present in the inventory")
         else: 
             inventory[sale_name]["quantity"] -= sale_quantity
             inventory[sale_name]["price"] = sale_price
    
    elif action == "list":
        for name in inventory:
            quantity = inventory[name]["quantity"]
            price = inventory[name]["price"]
            print(f"Product name: {name}| Quantity: {quantity} | Price: {price}")
    
    elif action == "warehouse":
        name = input("Enter the product name: ")
        if name not in inventory:
            print(f"{name}: not found.")
        else: 
            print(f" Product name: {name}")
            print(f" Quantity: {quantity}")
            print(f" Price:  {price}")

    elif action == "balance":
        name = input("Enter the product name: ")
        if name not in inventory:
            print(f"{name}: not found.")
        else: 
            revenue = float((sale_price * sale_quantity) - (purchase_price * purchase_quantity))
        print(50 * "-")
        # Ask how much money add into the business and then calculation 
    
    elif action == "account":
        print(f"Name: {purchase_name} | Earning: {revenue}")
    
    """elif action == "review":"""