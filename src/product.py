import uuid
from .category import Category


class Product:
    """
    Represents a product in the inventory.

    Attributes:
        id (str): Unique SKU assigned to the product.
        name (str): Product name.
        price (float): Product price.
        category (Category): The category the product belongs to.
        quantity (int): The number of units available in stock.
    """

    def __init__(self, name: str, price: float, category: Category, quantity: int):
        """
        Initializes a Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            category (Category): The category the product belongs to.
            quantity (int): Initial stock quantity.

        Raises:
            TypeError: If category is not a Category object.
            ValueError: If price or quantity is negative.
        """
        self.id: str = str(uuid.uuid4())  # Generate unique SKU
        self.name: str = name
        self.price: float = price
        self.category: Category = category
        self.quantity: int = quantity

    def get_details(self) -> dict:
        """
        Retrieves product details.

        Returns:
            dict: A dictionary containing product details.
        """
        return {
            "ID": self.id,
            "Name": self.name,
            "Price": self.price,
            "Category": self.category.name if self.category else "Uncategorized",
            "Quantity": self.quantity,
        }

    def update_price(self, new_price: float):
        """
        Updates the product's price.

        Args:
            new_price (float): The new price to be set.

        Raises:
            ValueError: If the new price is negative.
        """
        if new_price >= 0:
            self.price = new_price
        else:
            raise ValueError("Price cannot be negative.")

    def update_quantity(self, quantity_change: int):
        """
        Updates the product's stock quantity.

        Args:
            quantity_change (int): The amount to add or remove from stock.

        Raises:
            ValueError: If quantity goes below zero.
        """
        if self.quantity + quantity_change >= 0:
            self.quantity += quantity_change
        else:
            raise ValueError("Insufficient stock.")

    def __str__(self):
        """Returns a readable string representation of the product."""
        return f"Product[ID={self.id}, Name={self.name}, Price=${self.price:.2f}, Category={self.category.name}, Quantity={self.quantity}]"
