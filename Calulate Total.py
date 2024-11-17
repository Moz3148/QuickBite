# Calculate the total cost
def calculate_total(cart, menu):
    total = 0
    for item_name, quantity in cart.items():
        for item in menu:
            if item['name'].lower() == item_name:  # Compare lowercase names
                total += item['price'] * quantity
    return total