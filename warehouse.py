import warehouse_import

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
        pname = input("Adding the purchase item (name): ")
        pquantity = float(input(f"Please enter the {pname} quantities: "))
        pprice = float(input(f"Please enter the {pname} unit price: "))
        purchase = pprice * pquantity
        business_account -= purchase
        if pname not in inventory:
            inventory[pname] = {"quantity": 0.0, "quantity": 0}
            
            inventory[pname] ["quantity"] += pquantity
            inventory[pname]["price"] = pprice

            print(50 * "-")
            history.append(f"Purchase name: {pname}, purchase price: {pprice}, purcchase quantity: {pquantity}")

    elif action == "sale":
        sname = input("Please enter the sale item name: ")
        squantity = float(input(f"Please enter the {sname} quantities: "))
        sprice = float(input(f"Please enter the {sname} price: "))
        sale = sprice * squantity
        business_account += sale
        print(50 * "-")
        if sname not in inventory or inventory[sname]["quantity"] < 1: 
            print(f"{sname} not present in the inventory")
        else:
            inventory[sname]["quantity"] -= squantity
            inventory[sname]["price"] = sprice

            print(50 * "-")
            history.append(f"sale name: {sname}, purchase price: {sprice}, purcchase quantity: {squantity}")

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

        if from_value == "" and to_value == "":
            for i in history [from_value:to_value]: 
                print(i)
        elif from_value !="" and to_value =="":
            for i in history[int(from_value)-1:]:
                print(i)
        elif from_value =="" and to_value !="":
            for i in history[int(from_value)+1:]:
                print(i)
        else: 
            for i in history[int(from_value)-1:int(to_value)]:
                print(i)