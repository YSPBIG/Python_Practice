inventory = {}

def add_item(item,quantity):
    if item in inventory:
        inventory[item] += quantity  #+= is to add the values and variables
    else:
        inventory[item] = quantity
    print(f"Added {quantity} {item}.")

def view_inventory():
    for item,quantity in inventory.items():
        print(f"{item} : {quantity}")

def update_item(item,quantity):
    if item in inventory:
        inventory[item] = quantity
        print(f"Update the inventory {item} : {quantity}.")
    else:
        print("inventory not found")

def manage_inventory() :
    while True:
        print("Inventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Please enter choice (1/2/3/4) : ")

        if choice == "1":
            item = input("Enter the item : ")
            quantity = int(input("Enter the quantity : "))
            add_item(item,quantity)
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            item = input("Enter the item : ")
            quantity = int(input("Enter the new quantity : "))
            update_item(item,quantity)
        elif choice == "4":
            print("Exit")
            break
        else:
            print("Error, Please re-enter the operation")

manage_inventory()



                




