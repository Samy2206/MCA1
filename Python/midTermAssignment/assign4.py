# Write a python program where create a package “productorderdetails” in which 
# first module should accept order details, second module should do the price
# calculation and third must display order placed successfully .Note if total
# shopping is of more than 1000 rupees than discount be given of 12% on total
# purchase. Import all the following module to another package importData

# importData/main.py

from order import orderdetails, pricecalculation, ordersuccess

def order():
    # Accept order details
    product_name, quantity, price_per_unit = orderdetails.accept_order_details()
    
    # Calculate total price
    total_price = pricecalculation.calculate_price(quantity, price_per_unit)
    
    # Display the total price
    print(f"\nTotal price for {product_name} is: {total_price}")
    
    # Display order success message
    ordersuccess.display_order_success()

order()