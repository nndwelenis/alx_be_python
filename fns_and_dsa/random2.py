# Define the Product class
class Product:
    # Constructor that sets up each new product with a name, price, and quantity
    def __init__(self, name, price, quantity):
        self.name = name          # Store the product name
        self.price = price        # Store the product price per unit
        self.quantity = quantity  # Store how many units are in stock

    # Method to calculate the total value of the product in stock
    def total_value(self):
        # Multiply price by quantity to get value of all items combined
        return self.price * self.quantity


# Create a Product object
product1 = Product("Laptop", 12000, 5)

# Calculate the total value by calling the method
value = product1.total_value()

# Display the result
print(f"The total stock value for {product1.name} is R{value}")
