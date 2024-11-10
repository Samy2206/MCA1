# productorderdetails/price_calculation.py

def calculate_price(order_details):
    total_price = order_details['quantity'] * order_details['price_per_item']
    
    if total_price > 1000:
        discount = 0.12 * total_price
        total_price -= discount
        print(f"A discount of 12% has been applied. Discount amount: {discount}")
    else:
        print("No discount applied.")
    
    order_details['total_price'] = total_price
    return order_details
