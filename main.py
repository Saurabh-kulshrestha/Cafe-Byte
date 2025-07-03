# main.py — Controls the logic and flow of the virtual coffee machine.
# It handles user input, resource checking, payment processing, and machine updates.

# Importing data and UI elements from game_data.py
from game_data import machine_resource,menu,logo,line,clr

# Displaying the coffee machine logo at the start
print(logo)

# Function to display the current status of resources in the machine
def show_resource():
    print(clr)  # Clear the screen before showing status
    print("📊 Here's the current status of the machine:")
    print(line)
    print(f"Water : {machine_resource['water']}ml")
    print(f"Milk : {machine_resource['milk']}ml")
    print(f"Coffee : {machine_resource['coffee']}grams")
    print(f"Money : ₹{machine_resource['money']}")
    print(line)

# Function to check whether enough resources are available to make the selected coffee
def check_resource(choice):
    iteration = 0
    finish_resource = []    # List to store any unavailable ingredients
    for item in ["water", "milk", "coffee"]:
        if (machine_resource[item]) >= (menu[choice][item]):
            iteration += 1
        else:
            finish_resource.append(item)

    # If any ingredient is missing, display a warning and return False
    if iteration < 3 :
        for resource in finish_resource:
            print(f"⚠️ Sorry, there is not enough {resource}.")
        return False
    else:
        return True # All required resources are available

# Function to handle the transaction: take payment, give change, update resources
def transaction(choice):
    # Display selected coffee and its cost
    print(f"\nYou selected {choice}☕. It costs ₹{menu[choice]['cost']}.")

    # Collect cash input from the user in Indian currency denominations
    print(line)
    print("💰 Please insert cash.")
    hundred = int(input("🧾 Enter number of ₹100 notes: "))
    fifty = int(input("🧾 Enter number of ₹50 notes: "))
    twenty = int(input("🧾 Enter number of ₹20 notes: "))
    ten = int(input("🧾 Enter number of ₹10 notes: "))
    total = (100 * hundred) + (50 * fifty) + (20 * twenty) + (10 * ten)
    print(line)

    # Compare total inserted amount with the coffee cost
    if total < menu[choice]["cost"]:
        print(f"❌ Sorry, that's not enough money. ₹{total} refunded. 💸")
    else:
        print("✅ Payment successful. ")

        # Return extra cash if overpaid
        if total > menu[choice]["cost"]:
            refund = total - menu[choice]["cost"]
            print(f"💵 Here's ₹{refund} in change. ")

        # Deduct used resources and update money in machine
        machine_resource["water"] -= menu[choice]["water"]
        machine_resource["milk"] -= menu[choice]["milk"]
        machine_resource["coffee"] -= menu[choice]["coffee"]
        machine_resource["money"] += menu[choice]["cost"]

        # Final success message
        print("☕ Enjoy your drink! 😋\n")

# --------- Main Program Loop Starts Here ---------
while True:
    print(line * 2)
    # Asking the user what they would like to order
    user_choice = input("What would you like? (espresso/latte/cappuccino):  ").lower()

    # If user selects a valid drink
    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        if check_resource(user_choice):  # Check resource availability
            transaction(user_choice)     # Process payment and make the drink
    
    # If user wants to turn off the machine
    elif user_choice == "off":
        print(clr)
        # Displaying the coffee machine logo at the start
        print(logo)
        print(line * 2)
        print("Turning off the coffee machine. Have a great day!")
        break

    # If user wants to view current machine status
    elif user_choice == "report":
        show_resource()
    
    # Handle invalid input (i.e., input not matching any valid command)
    else:
        print("❌ Invalid input! Please choose from espresso, latte, cappuccino.")
