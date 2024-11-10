# productorderdetails/order_display.py

def display_order_success(order_details):
    print("\nOrder placed successfully!")
    print("Order Summary:")
    print(f"Product Name: {order_details['product_name']}")
    print(f"Quantity: {order_details['quantity']}")
    print(f"Price per Item: {order_details['price_per_item']}")
    print(f"Total Price: {order_details['total_price']}")
