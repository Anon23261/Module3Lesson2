# Sample Order Data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 3),
    ("Diana", "Headphones", 1)
]

def print_order_details(orders):
    """
    Iterates over a list of customer orders, unpacks each tuple, and prints order details.
    
    Args:
        orders (list): A list of tuples, where each tuple contains:
                       (customer_name, product, quantity)
    """
    for customer_name, product, quantity in orders:
        print(f"Customer: {customer_name}\nProduct: {product}\nQuantity: {quantity}\n")

# Call the function with the sample data
print_order_details(orders)
