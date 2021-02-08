"""Code snippet. Not runnable."""
# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query

def get_price():
    """grabs the discounted price"""
    discount_factor = 0
    if base_price() > 1000:
        discount_factor = 0.95
    else:
        discount_factor = 0.98
    return base_price() * discount_factor

def base_price(quantity, item_price):
    """returns base price of product"""
    return quantity * item_price
