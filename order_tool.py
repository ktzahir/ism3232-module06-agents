# order_tool.py
# Author: Kazi Zahir
class OrderLookup:
    """A tool that knows about orders. It knows nothing about chatting."""

    def __init__(self, orders):
        """Store the orders this tool can look up."""
        self.orders = orders

    def find_order_id(self, text):
        """Return the first known order ID mentioned in text, or None."""
        for order_id in self.orders:
            if order_id in text.upper():
                return order_id
        return None

    def find_status(self, order_id):
        """Return the status of an order, or None if it doesn't exist."""
        if order_id in self.orders:
            return self.orders[order_id]
        return None
