from manager import database

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
inventory = database.load_inventory()
history = database.load_history()
balance = database.load_balance()
business_account = 0.0

while True: 
    print(COMMAND_LIST_MSG)
    print(f"Database Inventory {database.inventory}")
    print(f"Database History {database.history}")
    print(f"Database Balance {database.balance}")
    print(50 * "-")
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

        if balance > 0.0:
            print(f"Current account balance is {balance}")
            pname = input("Adding the purchase item (name): ")
            pprice = float(input(f"Please enter the {pname} unit price: "))
            pquantity = float(input(f"Please enter the {pname} quantities: "))
            amount_cost = pprice * pquantity
            print(50 * "-")
            print(f"From this item {pname}, make total purchase{amount_cost} amount")
            print(50 * "-")
            if amount_cost <= balance:
                database.execute("purchase", pname, amount_cost, pquantity)
                #balance = database.balance
                database.history.append(f"Purchase {pname} for {pquantity} with total purchase price {amount_cost}, balance changed to {database.balance}")
            else:
                print("Not enough balance to cover the purchase")
                break
        else:
            print("Not enough balance to cover the purchase")
            break

    elif action == "sale":
        sname = input("Please enter the sale item name: ")
        if sname in inventory:
            print (f"The item {sname} current available in the inventory {inventory}")
            squantity = float(input(f"Please enter the {sname} quantities: "))
            sprice = float(input(f"Please enter the {sname} price: "))
            sale = sprice * squantity
            print(50 * "-")
            print(f"From this item {sname}, make total sale {sale} amount")
            print(50 * "-")

            if sname not in inventory or inventory[sname]["quantity"] < squantity:
                print("Not enough item to sale")
                break 
            else:
                database.execute("sale", sname, squantity)
                balance = database.balance
                print("After sale, we have {} left in the inventory" .format(squantity),inventory[sname])
                print("Current balance is", balance)
                database.history.append(f"Sell {sname} for {squantity} with total sale price {sale}, balance changed to {balance}")

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
        print(50 * "-")
        database.execute("change_balance", balance_command)
        balance = database.balance
        database.history.append(f"{balance_command} {database.balance} to the account balance")
    
    elif action == "account":
        print(database.balance)

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

database.save_inventory()
database.save_history()
database.save_balance()