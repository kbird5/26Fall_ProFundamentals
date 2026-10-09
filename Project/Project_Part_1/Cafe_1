#Setting variables for cafe name, tax rate, and menu items with their prices.
cafe_name = "Python Café"
tax_rate = 0.08

menu = {
    "espresso": 3.00,
    "latte": 4.50,
    "cappuccino": 4.25,
    "mocha": 5.00,
    "muffin": 2.50,
    "croissant": 3.25,
}

order = []

#setting greet(names) function to print a welcome message with the café name and the customer's name, using an f-string.
def greet(name):
# Prints a welcome message with the café name and the customer's name, using an f-string.
    print(f"Welcome to {cafe_name}, {name}!")
# setting customer_name variable to input the customer's name and calling greet() function to print the welcome message.
customer_name = input("What is your name? ")
greet(customer_name)
#if rewards_member.lower() == "yes": setting rewards_member variable to input if the customer is a rewards member and setting is_member variable to True or False based on the input.
rewards_member = input("Are you a rewards member? (yes/no): ")
is_member = False
if rewards_member.lower() == "yes":
    is_member = True
    print("You are a member.")
elif rewards_member.lower() == "no":
    print("Would you like to become a member? (yes/no): ")
    if input().lower() == "yes":
        is_member = True
        print("You are now a member.")
    else:
        is_member = False
        print("You are not a member.")


#setting show_menu(menu) function to loop through menu.items() and print every item with its price.
def show_menu(menu):
# Loops through menu.items() and prints every item with its price.
    for item in menu.items():
        print(f"{item[0]}: ${item[1]:.2f}")

   ### quantity = int(input("How many {item} would you like to order? 0-5: ")) 
#setting calculate_subtotal(order, menu) function to loop through the order, add up each item's price from the menu, and return the total.
def calculate_subtotal(order, menu):
    # Loops through the order, adds up each item's price from the menu, and returns the total.
    subtotal = 0.0
    for item in order:
        subtotal += menu[item]
    return subtotal
#setting get_discount(subtotal, is_member) function to return the discount in dollars, using the discount rules below.
def get_discount(subtotal, is_member):
    # Returns the discount in dollars, using the discount rules below.
    if is_member and subtotal >= 20:
        return subtotal * 0.15
    elif is_member and subtotal >= 10:
        return subtotal * 0.10
    elif not is_member and subtotal >= 25:
        return subtotal * 0.05
    else:
        return 0.0

   # def print_receipt(name, order, menu, is_member):
   # Calls calculate_subtotal() and get_discount(), works out tax and the total, and prints the receipt.
#setting print_receipt(customer_name, order, menu, is_member) function to call calculate_subtotal() and get_discount(), work out tax and the total, and print the receipt.
def  print_receipt(customer_name, order, menu, is_member):
               subtotal = calculate_subtotal(order, menu)
               discount = get_discount(subtotal, is_member)
               discounted_subtotal = subtotal - discount
               tax = discounted_subtotal * tax_rate
               total = discounted_subtotal + tax
   
               print(f"---- Receipt for {cafe_name} ----")
               print(f"Customer: {customer_name}")
               for item in order:
                   print(f"{item}: ${menu[item]:.2f}")
               print(f"Subtotal: ${subtotal:.2f}")
               print(f"Discount: -${discount:.2f}")
               print(f"Tax: ${tax:.2f}")
               print(f"Total: ${total:.2f}")

#Getting the options set up for the user to select from, and calling the appropriate functions based on the user's choice.
while True:
    print("1. Show menu")
    print("2. Add an item to your order")
    print("3. Remove an item from your order")
    print("4. View your order")
    print("5. Checkout")

    choice = input("Please select an option (1-5): ")

    #choice 1 calls show_menu(menu) function to print the menu.
    if choice == "1":
        show_menu(menu)

    #choice 2 allows the user to add an item to their order, and checks if the item is in the menu.
    elif choice == "2":
        item = input("What would you like to add?: ").lower()
        if item in menu:
            qty_input = int(input(f"How many {item}s would you like to add? "))
            if 0 < qty_input <= 5:
                qty = int(qty_input)
                for _ in range(qty):
                    order.append(item)
                print(f"Added {qty} {item}(s) to your order.")
            else:
                print("Please enter a quantity between 1 and 5.")
        else:
            print(f"Sorry, {item} is not on the menu.")

    #Choice 3 allows the user to remove an item from their order.
    elif choice == "3":
        item = input("Enter the item you would like to remove: ").lower()
        if item in order:
            order.remove(item)
            print(f"1 {item} has been removed from your order.")
        else:
            print(f"{item} is not in your order.")

    #choice 4 allows the user to view their order, and calls the show_order(order, menu) function.
    elif choice == "4":
        def show_order(order, menu):
            if not order:
                print("Your order is empty.")
            else:
                print("---- Your Order ----")
                for item in order:
                    print(f"{item}: ${menu[item]:.2f}")

        show_order(order, menu)

    #choice 5 allows the user to checkout, and checks if the order is empty. It allows the user to print the receipt and exit the loop.
    elif choice == "5":
        if len(order) == 0:
            print("Your order is empty. Please add items before checking out.")
        else:
            print_receipt(customer_name, order, menu, is_member)
            if is_member:
                print(f"Thank you for being a member! Thanks for visiting, {customer_name}.")
            if not is_member:
                print(f"Would you like to become a member today, {customer_name}?")
            break

    else:
        print("Please select a valid option (1-5).")