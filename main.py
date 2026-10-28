# main.py
# Author: Kazi Zahir

from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup

# Sample order data
ORDERS = {
    "A100": "shipped",
    "A101": "processing",
    "A102": "delivered",
}

# Sample inventory data
STOCK = {
    "shoes": "in stock",
    "hoodie": "out of stock",
    "hat": "in stock",
}

# Create the tools
order_tool = OrderLookup(ORDERS)
stock_tool = StockLookup(STOCK)

# Create the chatbot
bot = SupportChatbot(
    "Sunny",
    "You are a friendly customer support chatbot.",
    order_tool,
    stock_tool,
)

# Start the chatbot
print("Welcome! You are chatting with Sunny.")
print("Type 'quit' to exit.")

while True:
    message = input("You: ")

    if message.lower() == "quit":
        break

    reply = bot.respond(message)
    print(f"Sunny: {reply}")
