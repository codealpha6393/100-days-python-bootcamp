print("Welcome to Python Pizz Deliveries!")
if (size := input("What size pizza do you want? S, M, or L: ").upper()) not in ["S", "M", "L"]:
    print("Invalid size selected. Please choose S, M, or L.")
    exit()
add_pepperoni = input("Do you want to add pepperoni? Y or N: ").upper()
if add_pepperoni not in ["Y", "N"]:
    print("Invalid selection. Please choose Y or N.")
    exit()
extra_cheese = input("Do you want to add extra cheese? Y or N: ").upper()
if extra_cheese not in ["Y", "N"]:
    print("Invalid selection. Please choose Y or N.")
    exit()      

# Ensure valid inputs for size, pepperoni, and cheese
print(f"Size selected: {size}")
print(f"Add pepperoni: {add_pepperoni}")
print(f"Add extra cheese: {extra_cheese}")  
# Calculate the bill based on size and toppings
bill = 0    
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

print(f"Your final bill is: ${bill}")