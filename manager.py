class Manager:
    def __init__(self):
        self.actions = {}

    def assign(self, name):
            def wrapper(func):
                self.actions[name] = func
            return wrapper
            
    def execute(self, name, *args, **kwargs):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self, *args, **kwargs)
             

   
    def load_inventory (self):
        self.inventory = {}
        with open("text/inventory_load.txt") as f:
            for row in f:
                name, price, quantity = row.strip().split(";")
                price = float(price)
                quantity =float(quantity)
                self.load_inventory[name] ={
                    "price": price,
                    "quantity": quantity
                }
        return self.inventory
    
    def save_inventory(self):
        with open("text/inventory_save.txt", "w") as f:
            for product_name, stats in self.inventory.items():
                f.write("{};{};{}\n".format(product_name, stats["price"], stats["quantity"]))
    
    def load_balance(self):
        self.balance = 0
        with open ("text/balance_load.txt") as f:
            for row in f:
                self.balance = float(row)
        return self.balance
    
    def save_balance(self):
        with open("text/balance_save.txt", "w") as f:
            f.write("{}\n".format(self.balance))
    
    def load_history(self):
        self.history = []
        with open("text/history_load.txt") as f:
            for row in f:
                self.history.append(row.strip())
        return self.history
    
    def save_history(self):
        with open ("text/history_save.txt", "w") as f:
            for row in self.history:
                f.write(f"{row}\n. format(self.history)")

database = Manager()

@database.assign("change_balance")
def change_balance(manager, balance_command):
    if balance_command == "add":
        added_amount = float(input("How much want to add to the balance? "))
        manager.balance += added_amount
        print ("Current amount balance is {}".format(manager.balance))
    elif balance_command == "subtract":
        if manager.balance > 0.0:
            subtract_amount = float(input("How much want to remove from balance?"))

            if subtract_amount > manager.balance:
                print("Not enough money to remove.")
                return
            else:
                manager.balance -= subtract_amount
                print("Current account balance is {} after subtract". format(manager.balance))

@database.assign("sale")
def sale (manager, product, squantity):
    manager.inventory[product]['quantity'] -= squantity
    manager.balance += squantity * manager.inventory[product]['price']
    return manager.balance, manager.inventory

@database.assign("purchase")
def purchase(manager, product, pquantity, pprice):
    inventory = {}
    if product in manager.inventory:
        manager.inventory[product]['quantity'] += pquantity
        print(manager.inventory)
        manager.balance -= pprice 
        print ("Current balance in the account is:".format (manager.balance))
    if product not in manager.inventory:
        print("We do not have this product in the warehouse.")
        quantity = pquantity
        manager.inventory[product] = {'quantity': quantity, 'price': pprice}
        manager.balance -= pprice 
        print(inventory)
        print("Current balance:",manager.balance)