import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from src.category import Category
from src.product_factory import ProductFactory
from src.inventory import InventoryManager


# Initialize Inventory Manager
inventory = InventoryManager()

# Sample Categories
electronics = Category("Electronics", "Devices and gadgets")
clothing = Category("Clothing", "Apparel and fashion")

# Sample Products
product1 = ProductFactory.create_product("Smartphone", 699.99, electronics, 10)
product2 = ProductFactory.create_product("T-Shirt", 19.99, clothing, 50)

# Add products to inventory
inventory.add_product(product1)
inventory.add_product(product2)


# GUI Setup
root = tk.Tk()
root.title("E-commerce Inventory Management")
root.geometry("700x500")


# **Function to Update Product Listbox**
def update_product_list():
    product_listbox.delete(0, tk.END)  # Clear listbox
    for product in inventory.products.values():
        product_listbox.insert(
            tk.END,
            f"ID={product.id}, Name={product.name}, Price=${product.price}, "
            f"Category={product.category.name}, Quantity={product.quantity}",
        )


# **Function to Add a Product**
def add_product():
    name = name_entry.get().strip()
    price = price_entry.get().strip()
    category_name = category_var.get().strip()
    quantity = quantity_entry.get().strip()

    # Validate inputs
    if not name or not price or not category_name or not quantity:
        messagebox.showerror("Error", "All fields must be filled!")
        return

    try:
        price = float(price)
        quantity = int(quantity)

        if category_name.lower() == "electronics":
            category = electronics
        elif category_name.lower() == "clothing":
            category = clothing
        else:
            messagebox.showerror(
                "Error", "Category must be 'Electronics' or 'Clothing'"
            )
            return

        new_product = ProductFactory.create_product(name, price, category, quantity)
        inventory.add_product(new_product)
        update_product_list()
        messagebox.showinfo("Success", "Product added successfully!")

    except ValueError:
        messagebox.showerror(
            "Error", "Price must be a number and Quantity must be an integer!"
        )


# **Function to Remove Selected Product**
def remove_product():
    selected = product_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a product to remove.")
        return

    selected_text = product_listbox.get(selected[0])
    product_id = selected_text.split(",")[0].split("=")[1].strip()  # Extract ID

    try:
        inventory.remove_product(product_id)
        update_product_list()
        messagebox.showinfo("Success", "Product removed successfully.")
    except ValueError:
        messagebox.showerror("Error", "Product not found.")


# **Function to Search Product by ID**
def search_product():
    product_id = search_entry.get().strip()
    if not product_id:
        messagebox.showerror("Error", "Enter a product ID to search.")
        return

    product = inventory.get_product_by_id(product_id)
    if product:
        messagebox.showinfo(
            "Product Found",
            f"ID={product.id}, Name={product.name}, Price=${product.price}, "
            f"Category={product.category.name}, Quantity={product.quantity}",
        )
    else:
        messagebox.showerror("Error", "Product not found.")


# **Function to Filter Products by Category**
def filter_by_category():
    category_name = category_filter_var.get().strip().lower()

    if category_name == "electronics":
        category = electronics
    elif category_name == "clothing":
        category = clothing
    else:
        messagebox.showerror("Error", "Please select 'Electronics' or 'Clothing'.")
        return

    filtered_products = inventory.get_products_by_category(category)

    product_listbox.delete(0, tk.END)  # Clear listbox
    if filtered_products:
        for product in filtered_products:
            product_listbox.insert(
                tk.END,
                f"ID={product.id}, Name={product.name}, Price=${product.price}, "
                f"Category={product.category.name}, Quantity={product.quantity}",
            )
    else:
        messagebox.showinfo("No Products", "No products found in this category.")


# **Create Frames for Better Organization**
frame1 = tk.Frame(root)
frame1.pack(pady=10)

frame2 = tk.Frame(root)
frame2.pack(pady=10)

frame3 = tk.Frame(root)
frame3.pack(pady=10)

frame4 = tk.Frame(root)
frame4.pack(pady=10)

# **Widgets**
product_listbox = tk.Listbox(root, width=100, height=10)
product_listbox.pack(pady=10)
update_product_list()  # Load initial product list


# **Add Product Section**
tk.Label(frame1, text="Add Product").grid(row=0, column=0, columnspan=2)

name_entry = tk.Entry(frame1, width=30)
name_entry.grid(row=1, column=0, padx=5, pady=5)
name_entry.insert(0, "Product Name")

price_entry = tk.Entry(frame1, width=20)
price_entry.grid(row=1, column=1, padx=5, pady=5)
price_entry.insert(0, "Price")

category_var = tk.StringVar(value="Electronics")
category_dropdown = tk.OptionMenu(frame1, category_var, "Electronics", "Clothing")
category_dropdown.grid(row=2, column=0, columnspan=2, pady=5)

quantity_entry = tk.Entry(frame1, width=20)
quantity_entry.grid(row=3, column=0, columnspan=2, pady=5)
quantity_entry.insert(0, "Quantity")

add_button = tk.Button(frame1, text="Add Product", command=add_product)
add_button.grid(row=4, column=0, columnspan=2, pady=10)


# **Remove Product Button**
remove_button = tk.Button(
    frame2, text="Remove Selected Product", command=remove_product
)
remove_button.grid(row=0, column=0, padx=5, pady=5)


# **Search Product by ID**
tk.Label(frame3, text="Search Product by ID").grid(row=0, column=0)

search_entry = tk.Entry(frame3, width=20)
search_entry.grid(row=0, column=1, padx=5, pady=5)
search_button = tk.Button(frame3, text="Search", command=search_product)
search_button.grid(row=0, column=2, padx=5, pady=5)


# **Filter by Category**
tk.Label(frame4, text="Filter by Category").grid(row=0, column=0)

category_filter_var = tk.StringVar(value="Electronics")
category_filter_dropdown = tk.OptionMenu(
    frame4, category_filter_var, "Electronics", "Clothing"
)
category_filter_dropdown.grid(row=0, column=1, padx=5, pady=5)

filter_button = tk.Button(frame4, text="Filter", command=filter_by_category)
filter_button.grid(row=0, column=2, padx=5, pady=5)


# **Run the Tkinter Main Loop**
root.mainloop()
