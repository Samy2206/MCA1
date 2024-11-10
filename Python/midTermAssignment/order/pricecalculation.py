# productorderdetails/pricecalculation.py

def calculate_price(quantity, price_per_unit):
    total_price = quantity * price_per_unit
    
    # Applying discount if total price is more than 1000
    if total_price > 1000:
        discount = total_price * 0.12
        total_price -= discount
        print(f"A discount of 12% is applied. Discount Amount: {discount}")
    
    return total_price
