# stock_tool.py
# Author: Kazi Zahir


class StockLookup:
    """A tool that checks product availability."""

    def __init__(self, stock):
        """Store the product inventory."""
        self.stock = stock

    def find_product(self, text):
        """Find a known product mentioned in the customer's message."""
        for product in self.stock:
            if product.lower() in text.lower():
                return product
        return None

    def find_status(self, product):
        """Return the availability of a product."""
        if product in self.stock:
            return self.stock[product]
        return None
