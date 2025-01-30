# E-commerce Inventory Management System

## Overview
This project is a simple **E-commerce Inventory Management System** built using **Python**. It follows **Object-Oriented Programming (OOP) principles**, implements a **factory design pattern**, and adheres to **software engineering best practices**. The system allows managing products, their categories, and inventory.

## Features
- **Product Management**: Create, update, and retrieve product details.
- **Category Management**: Organize products into categories.
- **Inventory Management**: Add, remove, and retrieve products from inventory.
- **Design Patterns**: Implements the **Factory Pattern** to manage product creation.
- **Error Handling**: Meaningful error messages for invalid operations.
- **Testing**: Unit tests using `pytest` to ensure code reliability.

## Installation
### Prerequisites
- Python **>=3.9**
- `pip` package manager

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/singhsagar27/ecommerce-inventory.git
   cd ecommerce-inventory
   ```

2. **Create and activate a virtual environment**  
   - On **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install pre-commit hooks**
   ```bash
   pre-commit install
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

6. **(Optional) Deactivate the virtual environment**  
   ```bash
   deactivate
   ```

## Project Structure
```
.
├── src/
│   ├── product.py           # Product class
│   ├── category.py          # Category class
│   ├── inventor.py          # Inventory management
│   ├── product_factory.py   # Factory Pattern implementation
│
├── tests/
│   ├── test_product.py
│   ├── test_category.py
│   ├── test_inventory.py
│   ├── test_factory.py
│
├── requirements.txt
├── README.md
└── main.py
```

## Design Pattern: Factory
This project uses the **Factory Pattern** to create products. The `ProductFactory` class ensures **proper validation** and centralizes product creation, making it easier to extend in the future.

### Implementation (Snippet)
```python
from product import Product
from category import Category
import uuid

class ProductFactory:
    @staticmethod
    def create_product(name: str, price: float, category: Category, quantity: int) -> Product:
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        return Product(str(uuid.uuid4()), name, price, category, quantity)
```

## Testing
This project uses `pytest` for unit testing. To run tests, execute:
```bash
pytest --cov=src tests/
```

## Code Quality
- Code follows **PEP8 standards**.
- The project uses pre-commit hooks to automatically run linting and formatting tools (such as `flake8`, `black`) on each commit. The hooks will be installed and activated when you run `pre-commit install`.

## License
MIT License

## Author
Sagar Singh - [GitHub Profile](https://github.com/singhsagar27)

