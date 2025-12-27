from datetime import datetime

# Menu dictionary
menu = {
    'Pizza': 40,
    'Burger': 20,
    'Fries': 20,
    'Coke': 25,
    'Coffee': 50,
    'Pasta': 30
}

GST_RATE = 0.05
DISCOUNT_RATE = 0.10
DISCOUNT_THRESHOLD = 200


def display_menu():
    print("\n----- MENU -----")
    for item, price in menu.items():
        print(f"{item}: Rs{price}")
    print("----------------")


def take_orders():
    order = {}

    while True:
        item = input("\nEnter item name (or 'done' to finish): ").strip().title()

        if item == "Done":
            break

        if item not in menu:
            print("❌ Item not available. Please choose from the menu.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {item}: "))
            if quantity <= 0:
                print("❌ Quantity must be greater than zero.")
                continue
        except ValueError:
            print("❌ Please enter a valid number for quantity.")
            continue

        if item in order:
            order[item] += quantity
        else:
            order[item] = quantity

        print(f"✅ {item} x {quantity} added to order.")

    return order


def generate_bill(order):
    print("\n=========== BILL RECEIPT ===========")
    print("Bharti's Restaurant")
    print("Date & Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print("----------------------------------")

    subtotal = 0

    for item, qty in order.items():
        price = menu[item] * qty
        subtotal += price
        print(f"{item} x {qty} = Rs{price}")

    print("----------------------------------")
    print(f"Subtotal: Rs{subtotal}")

    gst = subtotal * GST_RATE
    print(f"GST (5%): Rs{gst:.2f}")

    discount = 0
    if subtotal >= DISCOUNT_THRESHOLD:
        discount = subtotal * DISCOUNT_RATE
        print(f"Discount (10%): -Rs{discount:.2f}")

    total = subtotal + gst - discount
    print("----------------------------------")
    print(f"TOTAL AMOUNT: Rs{total:.2f}")
    print("=========== THANK YOU ==============")


def main():
    print("Welcome to Bharti's Restaurant")
    display_menu()

    order = take_orders()

    if not order:
        print("\nNo items ordered. Thank you for visiting!")
    else:
        generate_bill(order)


if __name__ == "__main__":
    main()

