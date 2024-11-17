# Display the menu
def display_menu(menu):
    print("Menu:")
    for item in menu:
        print(f"{item['name']}: ${item['price']}")
