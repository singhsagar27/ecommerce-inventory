import unittest
from src.product import Product
from src.category import Category
from src.product_factory import ProductFactory


class TestProductFactory(unittest.TestCase):

    def setUp(self):
        """Set up a test category before each test."""
        self.category = Category("Electronics", "Electronic gadgets")

    def test_product_factory_creation(self):
        """Test if product factory creates a product correctly."""
        product = ProductFactory.create_product("Smartphone", 700, self.category, 10)
        self.assertIsInstance(product, Product)
        self.assertEqual(product.name, "Smartphone")
        self.assertEqual(product.price, 700)
        self.assertEqual(product.category.name, "Electronics")
        self.assertEqual(product.quantity, 10)

    def test_product_factory_invalid_price(self):
        """Test product factory with negative price should raise ValueError."""
        with self.assertRaises(ValueError):
            ProductFactory.create_product("Tablet", -100, self.category, 5)

    def test_product_factory_invalid_quantity(self):
        """Test product factory with negative quantity should raise ValueError."""
        with self.assertRaises(ValueError):
            ProductFactory.create_product("Headphones", 150, self.category, -2)


if __name__ == "__main__":
    unittest.main()
