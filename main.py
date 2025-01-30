import sys
from src.category import Category
from src.product_factory import ProductFactory
from src.inventory import InventoryManager


def main():
    """
    Entry point of the E-commerce Inventory Management System.
    Provides a simple command-line interface for inventory operations.
    """
    inventory = InventoryManager()

    # Sample categories
    electronics = Category("Electronics", "Devices and gadgets")
    clothing = Category("Clothing", "Apparel and fashion")

    # Sample products
    product1 = ProductFactory.create_product("Smartphone", 699.99, electronics, 10)
    product2 = ProductFactory.create_product("T-Shirt", 19.99, clothing, 50)

    # Add products to inventory
    inventory.add_product(product1)
    inventory.add_product(product2)

    while True:
        print("\nE-commerce Inventory Management System")
        print("1. View All Products")
        print("2. Add Product")
        print("3. Remove Product")
        print("4. Search Product by ID")
        print("5. View Products by Category")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            products = inventory.get_all_products()
            for product in products:
                print(product)

        elif choice == "2":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            category_name = input("Enter category (Electronics/Clothing): ")
            quantity = int(input("Enter quantity: "))

            category = (
                electronics if category_name.lower() == "electronics" else clothing
            )
            new_product = ProductFactory.create_product(name, price, category, quantity)
            inventory.add_product(new_product)
            print("Product added successfully.")

        elif choice == "3":
            product_id = input("Enter product ID to remove: ")
            try:
                inventory.remove_product(product_id)
                print("Product removed successfully.")
            except ValueError as e:
                print(e)

        elif choice == "4":
            product_id = input("Enter product ID: ")
            product = inventory.get_product_by_id(product_id)
            if product:
                print(product)
            else:
                print("Product not found.")

        elif choice == "5":
            category_name = input("Enter category (Electronics/Clothing): ")
            category = (
                electronics if category_name.lower() == "electronics" else clothing
            )
            products = inventory.get_products_by_category(category)
            if products:
                for product in products:
                    print(product)
            else:
                print("No products found in this category.")

        elif choice == "6":
            print("Exiting the system.")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
