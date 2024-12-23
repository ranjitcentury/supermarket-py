products = {
    "Apple": {"price": 1.2, "quantity": 50},
    "Banana": {"price": 0.5, "quantity": 100},
    "Orange": {"price": 1.0, "quantity": 30},
    "Milk": {"price": 1.5, "quantity": 20},
    "Bread": {"price": 2.0, "quantity": 15}
}

def display_products():
    print("Available Products:")
    for product, details in products.items():
        print(f"{product}: Price = ${details['price']} | Quantity = {details['quantity']}")

def update_stock(product, quantity):
    if products[product]["quantity"] >= quantity:
        products[product]["quantity"] -= quantity
        return True
    else:
        return False

def generate_receipt(cart):
    print("\nReceipt:")
    total = 0
    for item, quantity in cart.items():
        price = products[item]["price"]
        print(f"{item} x {quantity} = ${price * quantity}")
        total += price * quantity
    print(f"\nTotal Amount: ${total}")
    return total

def supermarket_system():
    cart = {}
    while True:
        display_products()
        product = input("\nEnter the product you want to buy (or type 'exit' to finish): ").capitalize()
        if product == 'Exit':
            break

        if product in products:
            quantity = int(input(f"Enter quantity for {product}: "))

            if update_stock(product, quantity):
                if product in cart:
                    cart[product] += quantity
                else:
                    cart[product] = quantity
                print(f"{quantity} {product}(s) added to your cart.")
            else:
                print(f"Sorry, not enough stock for {product}.")
        else:
            print("Invalid product. Please choose from the available products.")

    total = generate_receipt(cart)
    print(f"Thank you for shopping! Total amount: ${total}")

supermarket_system()
