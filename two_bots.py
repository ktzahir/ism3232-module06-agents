# two_bots.py
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


# Create the first chatbot: Sunny
sunny = SupportChatbot(
    "Sunny",
    "You are a friendly customer support chatbot.",
    order_tool,
    stock_tool,
)

# Create the second chatbot: River
river = SupportChatbot(
    "River",
    "You are a helpful customer support chatbot.",
    order_tool,
    stock_tool,
)


# Send messages to Sunny
print("=== Sunny's Conversation ===")
print("User: hello")
print("Sunny:", sunny.respond("hello"))

print("User: Where is my order A100?")
print("Sunny:", sunny.respond("Where is my order A100?"))


# Send messages to River
print("\n=== River's Conversation ===")
print("User: Are the shoes available?")
print("River:", river.respond("Are the shoes available?"))

print("User: I need to change my payment")
print("River:", river.respond("I need to change my payment"))


# Check conversation histories
print("\n=== Conversation History ===")
print("Sunny's history:", sunny.history)
print("River's history:", river.history)


# Count user messages
print("\n=== Message Counts ===")
print("Sunny's user messages:", sunny.count_user_messages())
print("River's user messages:", river.count_user_messages())


# Verify the chatbots are separate objects
print("\n=== Object Independence ===")
print("Are Sunny and River different objects?", sunny is not river)
print("Do they have separate histories?", sunny.history is not river.history)
