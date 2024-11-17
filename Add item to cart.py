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