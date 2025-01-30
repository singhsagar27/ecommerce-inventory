import unittest
from src.product import Product
from src.category import Category
from src.inventory import InventoryManager


class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        """Set up test inventory and products."""
        self.inventory = InventoryManager()
        self.category = Category("Electronics", "Electronic gadgets")
        self.product1 = Product("Laptop", 1200, self.category, 5)
        self.product2 = Product("Smartphone", 800, self.category, 8)

    def test_add_product(self):
        """Test adding a product to inventory."""
        self.inventory.add_product(self.product1)
        self.assertEqual(len(self.inventory.get_all_products()), 1)

    def test_add_duplicate_product(self):
        """Test adding a product with the same SKU should raise ValueError."""
        self.inventory.add_product(self.product1)
        with self.assertRaises(ValueError):
            self.inventory.add_product(self.product1)

    def test_remove_product(self):
        """Test removing a product from inventory."""
        self.inventory.add_product(self.product1)
        self.inventory.remove_product(self.product1.id)
        self.assertEqual(len(self.inventory.get_all_products()), 0)

    def test_remove_nonexistent_product(self):
        """Test removing a non-existing product should raise ValueError."""
        with self.assertRaises(ValueError):
            self.inventory.remove_product("invalid_sku")

    def test_get_product_by_id(self):
        """Test retrieving a product by ID."""
        self.inventory.add_product(self.product1)
        retrieved_product = self.inventory.get_product_by_id(self.product1.id)
        self.assertEqual(retrieved_product.name, "Laptop")

    def test_get_products_by_category(self):
        """Test retrieving products by category."""
        self.inventory.add_product(self.product1)
        self.inventory.add_product(self.product2)
        products = self.inventory.get_products_by_category(self.category)
        self.assertEqual(len(products), 2)


if __name__ == "__main__":
    unittest.main()
