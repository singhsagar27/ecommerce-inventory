import unittest
from src.product import Product
from src.category import Category


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Set up a test product before each test."""
        self.category = Category("Electronics", "Electronic gadgets and devices")
        self.product = Product("Laptop", 1200.50, self.category, 10)

    def test_product_creation(self):
        """Test if product is created correctly."""
        self.assertEqual(self.product.name, "Laptop")
        self.assertEqual(self.product.price, 1200.50)
        self.assertEqual(self.product.category.name, "Electronics")
        self.assertEqual(self.product.quantity, 10)

    def test_product_price_update(self):
        """Test updating product price."""
        self.product.update_price(999.99)
        self.assertEqual(self.product.price, 999.99)

    def test_product_price_update_invalid(self):
        """Test updating product price with negative value should raise ValueError."""
        with self.assertRaises(ValueError):
            self.product.update_price(-50)

    def test_product_quantity_update(self):
        """Test updating product quantity."""
        self.product.update_quantity(5)
        self.assertEqual(self.product.quantity, 15)

    def test_product_quantity_update_invalid(self):
        """Test reducing quantity below zero should raise ValueError."""
        with self.assertRaises(ValueError):
            self.product.update_quantity(-15)

    def test_product_details(self):
        """Test if get_details returns correct information."""
        details = self.product.get_details()
        self.assertEqual(details["Name"], "Laptop")
        self.assertEqual(details["Category"], "Electronics")


if __name__ == "__main__":
    unittest.main()
