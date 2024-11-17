# Define the menu and cart
menu = [
    {"name": "Tandoori", "price": 4.99},
    {"name": "Mix Grill", "price": 9.99},
    {"name": "Biryani", "price": 7.50},
    {"name": "Chicken Tikka", "price": 5.50},
    {"name": "Salad", "price": 3.50}
]
cart = {}

# Display the menu
def display_menu(menu):
    print("Menu:")
    for item in menu:
        print(f"{item['name']}: ${item['price']}")

# Add item to cart (case-insensitive)
def add_to_cart(item_name, menu, cart):
    item_name = item_name.strip().lower()  # Convert input to lowercase
    for item in menu:
        if item['name'].lower() == item_name:  # Compare lowercase names
            if item_name in cart:
                cart[item_name] += 1
            else:
                cart[item_name] = 1
            print(f"{item['name']} added to cart.")
            return
    print("Item not available.")

# Calculate the total cost
def calculate_total(cart, menu):
    total = 0
    for item_name, quantity in cart.items():
        for item in menu:
            if item['name'].lower() == item_name:  # Compare lowercase names
                total += item['price'] * quantity
    return total

# Main ordering function
def order_food():
    print("Welcome to QuickBite Mr Ali !!")
    display_menu(menu)

    while True:
        item_name = input("Enter item name to add to cart (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        add_to_cart(item_name, menu, cart)

    print("\nYour cart:", cart)
    total_cost = calculate_total(cart, menu)
    print(f"Total Cost: ${total_cost:.2f}")

    confirm = input("Confirm order? (yes/no): ")
    if confirm.lower() == 'yes':
        print("Thank you for your order!")
    else:
        print("Order canceled.")

# Run the order function
order_food()
