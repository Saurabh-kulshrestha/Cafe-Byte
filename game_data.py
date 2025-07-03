# This file defines the coffee machine's starting resources, available drinks, and display elements.

# Initial available resources in the coffee machine (in ml, grams, and rupees)
machine_resource = {
    "water" : 300,    #ml
    "milk" : 200,     #ml
    "coffee" : 100,   #grams
    "money" : 50     #rupee     
}

# Menu containing drink options with required ingredients and their cost (in ₹)
menu = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "cost": 130
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 150
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 180
    }
}

# Project logo (ASCII art) displayed when the machine starts
logo = r'''

   ___       __          ___       _       
  / __\__ _ / _| ___    / __\_   _| |_ ___ 
 / /  / _` | |_ / _ \  /__\// | | | __/ _ \
/ /__| (_| |  _|  __/ / \/  \ |_| | ||  __/
\____/\__,_|_|  \___| \_____/\__, |\__\___|
                             |___/         

😋 Sip, smile, and enjoy your virtual café!
'''

# Divider line used for neat output formatting
line = "-"*50

# Clear screen by printing 50 new lines (used for visual reset)
clr = "\n"*50