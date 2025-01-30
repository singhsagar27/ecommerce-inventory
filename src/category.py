class Category:
    """
    Represents a product category.

    Attributes:
        name (str): The name of the category.
        description (str): A short description of the category.
    """

    def __init__(self, name: str, description: str):
        """
        Initializes a Category instance.

        Args:
            name (str): The name of the category.
            description (str): A short description of the category.
        """
        self.name = name
        self.description = description

    def get_details(self) -> dict[str, str]:
        """
        Retrieves category details.

        Returns:
            dict: A dictionary containing the category's name and description.
        """
        return {"Name": self.name, "Description": self.description}

    def __str__(self) -> str:
        """Returns a readable string representation of the category."""
        return f"Category[Name={self.name}, Description={self.description}]"
