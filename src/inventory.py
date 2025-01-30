from .product import Product
from .category import Category


class InventoryManager:
    def __init__(self):
        """
        Manages a collection of products in an inventory.

        Attributes:
            products (dict): A dictionary storing products with SKU as key.
        """
        self.products = {}  # SKU -> Product object

    def add_product(self, product):
        """
        Adds a new product to the inventory.

        Args:
            product (Product): The product to be added.

        Raises:
            TypeError: If the argument is not a Product instance.
            ValueError: If the product SKU already exists.
        """
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added to inventory.")
        if product.id in self.products:
            raise ValueError(f"Product with SKU {product.id} already exists.")
        self.products[product.id] = product

    def remove_product(self, product_id):
        """
        Removes a product from inventory.

        Args:
            product_id (str): The SKU of the product to be removed.

        Raises:
            ValueError: If the product does not exist.
        """
        if product_id in self.products:
            del self.products[product_id]
        else:
            raise ValueError("Product not found.")

    def get_product_by_id(self, product_id):
        """
        Retrieves a product by its SKU.

        Args:
            product_id (str): The SKU of the product.

        Returns:
            Product or None: The product object if found, otherwise None.
        """
        return self.products.get(product_id, None)

    def get_all_products(self):
        """
        Retrieves all products in inventory.

        Returns:
            list: A list of all products in the inventory.
        """

        return list(self.products.values())

    def get_products_by_category(self, category) -> list[Product]:
        """
        Retrieves all products belonging to a specific category.

        Args:
            category (Category): The category to filter products by.

        Returns:
            list: A list of products in the given category.

        Raises:
            TypeError: If the category argument is not a Category instance.
        """
        if not isinstance(category, Category):
            raise TypeError("Expected a Category object.")
        return [
            product
            for product in self.products.values()
            if product.category == category
        ]

    def __str__(self):
        """Returns a readable string representation of the inventory."""
        return f"Inventory[Total Products={len(self.products)}]"
