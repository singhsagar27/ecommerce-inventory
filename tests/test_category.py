import unittest
from src.category import Category


class TestCategory(unittest.TestCase):

    def setUp(self):
        """Set up a test category before each test."""
        self.category = Category("Electronics", "Electronic gadgets and devices")

    def test_category_creation(self):
        """Test if category is created correctly."""
        self.assertEqual(self.category.name, "Electronics")
        self.assertEqual(self.category.description, "Electronic gadgets and devices")

    def test_category_details(self):
        """Test if get_details returns correct information."""
        details = self.category.get_details()
        self.assertEqual(details["Name"], "Electronics")
        self.assertEqual(details["Description"], "Electronic gadgets and devices")


if __name__ == "__main__":
    unittest.main()
