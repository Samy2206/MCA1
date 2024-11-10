# productorderdetails/order_input.py

def accept_order():
    order_details = {}
    order_details['product_name'] = input("Enter the product name: ")
    order_details['quantity'] = int(input("Enter the quantity: "))
    order_details['price_per_item'] = float(input("Enter the price per item: "))
    return order_details
