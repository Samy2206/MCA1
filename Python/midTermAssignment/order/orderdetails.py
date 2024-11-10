# productorderdetails/orderdetails.py

def accept_order_details():
    print("Enter order details:")
    product_name = input("Product name: ")
    quantity = int(input(f"Quantity of {product_name}: "))
    price_per_unit = float(input(f"Price per unit of {product_name}: "))
    
    return product_name, quantity, price_per_unit
