from .product import Product
from .category import Category
import uuid


class ProductFactory:
    """
    Factory Pattern Implementation for Product Creation.

    - The Factory Pattern is used to centralize product creation.
    - It ensures all products are validated before they are instantiated.
    - This prevents direct instantiation errors and allows for future extensibility.

    Example Usage:
        electronics = Category("Electronics", "Devices and gadgets")
        laptop = ProductFactory.create_product("Laptop", 1200.00, electronics, 5)
    """

    @staticmethod
    def create_product(
        name: str, price: float, category: Category, quantity: int
    ) -> Product:
        """Creates a new Product instance after validation."""
        if not isinstance(category, Category):
            raise TypeError("Category must be a Category object.")

        if price < 0:
            raise ValueError("Price cannot be negative.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        return Product(name, price, category, quantity)
