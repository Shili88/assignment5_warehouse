"""
simulates operations on a company'account and a warehouse
adding/subtracting balance, recoding sales, purhcases, display account balance, showing warehouse status and reviewing the recoded operations 
"""

# balance -  amount to add or subtract from the account
# sale -  name of the product, its price, and quantity - update the account and warehouse 
# purchase - name of the product, its price, and quantity - calculations and update the account and warehouse - account balance is not negative after a purchase operation.
# account - Display the current account balance.
# list - total inventory in the warehouse along with product prices and quantities
# warehouse -  product name and display its status in the warehouse.
# review -  two indices 'from' and 'to', and display all recorded operations within that range -  If ‘from’ and ‘to’ are empty, display all recorder operations. Handle cases where 'from' and 'to' values are out of range.
# end - Terminate the program.
# display the list of commands and prompt for the next command. 

balance = 0 
sale = 0 
purchase = 0 
account = 0 

product_name = input("Please enter the product name: ")
product_price = float(input("please enter the product price: ")) 