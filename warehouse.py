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
balance = {}
business_account = 0 
history = []

while True: 
    print(COMMAND_LIST_MSG)
    print(inventory)
    print(balance)
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
        
        print(50 * "-")
        history.append(f"Purchase name: {purchase_name}, purchase price: {purchase_price}, purcchase quantity: {purchase_quantity}")

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
             
             print(50 * "-")
             history.append(f"sale name: {sale_name}, purchase price: {sale_price}, purcchase quantity: {sale_quantity}")


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
            print(f" Quantity: {inventory[name]["quantity"]}")
            print(f" Price:  {inventory[name]["price"]}")

    elif action == "balance":
        balance_command = input("Please enter either want to 'add' or 'subtract' money from the account: ")
        amount = float(input("Enter an amount: "))
        print(50 * "-")
        if balance_command == "add":
            business_account += amount 
            if balance_command not in balance:
                balance[balance_command] = {"amount": 0.0, "amount": 0}
                balance[balance_command] ["amount"] += 1
                
                history.append(f"balance add the amount {amount}")

            print(50 * "-")
        elif balance_command == "subtract":
            if amount > business_account: 
                print(f"{amount}.No enough money to subtract from the account.")
            else: 
                business_account -= amount
                if balance_command not in balance:
                    balance[balance_command] = {"amount": 0.0, "amount": 0}
                    balance[balance_command] ["amount"] -= 1
                    
                    history.append(f"balance subtract the amount {amount}")

                print(50 * "-")
        else:
            print(f"The balance command you selected '{balance_command}' is not available.")
    
    elif action == "account":
        print(business_account)

# review -  If ‘from’ and ‘to’ are empty, display all recorder operations. Handle cases where 'from' and 'to' values are out of range. = create an history with the empty list. the empty list in the beginning. sale and balance and create history entry and to the list
    elif action == "review":
        from_value = int(input("Please enter the 'from' value: "))
        to_value = int (input("Please enter the 'to value': "))

        for i in history [from_value:to_value]: 
            print(i)