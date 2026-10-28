# tests/test_chatbot.py
# Author: Kazi Zahir

from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup

STOCK = {
    "shoes": "in stock",
    "hoodie": "out of stock",
    "hat": "in stock",
}


def create_bot():
    """Create a chatbot with order and stock lookup tools."""
    orders = {"A100": "shipped"}
    order_tool = OrderLookup(orders)
    stock_tool = StockLookup(STOCK)

    return SupportChatbot(
        "Sunny",
        "You are a friendly support chatbot.",
        order_tool,
        stock_tool,
    )


def test_find_order_id():
    orders = {"A100": "shipped"}
    tool = OrderLookup(orders)

    result = tool.find_order_id("Where is my order a100?")

    assert result == "A100"


def test_find_status():
    orders = {"A100": "shipped", "A101": "processing"}
    tool = OrderLookup(orders)

    result = tool.find_status("A101")

    assert result == "processing"


def test_unknown_order():
    orders = {"A100": "shipped"}
    tool = OrderLookup(orders)

    result = tool.find_status("A999")

    assert result is None


def test_chatbot_greeting():
    bot = create_bot()

    result = bot.respond("hello")

    assert result == "Hello! I'm Sunny. I can check an order status for you."


def test_chatbot_order_reply():
    bot = create_bot()

    result = bot.respond("Where is my order A100?")

    assert result == "Order A100 is shipped."


def test_chatbot_handoff():
    bot = create_bot()

    result = bot.respond("I need to change my payment")

    assert result == "I can't help with that here. I'm passing you to a human agent."


def test_chatbot_history():
    bot = create_bot()

    bot.respond("hello")

    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"


def test_chatbot_missing_order_id():
    bot = create_bot()

    result = bot.respond("Where is my order?")

    assert result == "Which order? Please send an order ID like A100."


def test_count_user_messages():
    bot = create_bot()

    bot.respond("hello")
    bot.respond("Where is my order A100?")

    assert bot.count_user_messages() == 2


def test_find_product():
    tool = StockLookup(STOCK)

    result = tool.find_product("Are the shoes available?")

    assert result == "shoes"


def test_stock_status():
    tool = StockLookup(STOCK)

    result = tool.find_status("hoodie")

    assert result == "out of stock"


def test_chatbot_stock_reply():
    bot = create_bot()

    result = bot.respond("Are the shoes available?")

    assert result == "Shoes is in stock."
