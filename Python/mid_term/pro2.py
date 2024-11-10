#python/pro2.py

from order.order_input import accept_order
from order.price_calculation import calculate_price
from order.order_display import display_order_success

def order():
    order_details = accept_order()
    
    order_details = calculate_price(order_details)
    
    display_order_success(order_details)

order()