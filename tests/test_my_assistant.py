from my_assistant import SoccerAssistant
from my_tool import SoccerSchedule


def create_bot():
    schedule = SoccerSchedule()
    return SoccerAssistant("MatchDay", schedule)


def test_pickup_schedule():
    bot = create_bot()
    response = bot.respond("Is there pickup soccer today?")
    assert "Tuesday" in response


def test_tournament_date():
    bot = create_bot()
    response = bot.respond("When is the next tournament?")
    assert "November 23, 2026" in response


def test_pickup_location():
    bot = create_bot()
    response = bot.respond("Where is pickup soccer?")
    assert "Fowler Fields" in response


def test_human_handoff():
    bot = create_bot()
    response = bot.respond("Can I change my team?")
    assert "SSA organizer" in response


def test_safe_fallback():
    bot = create_bot()
    response = bot.respond("What's the weather?")
    assert "not sure" in response


def test_conversation_history():
    bot = create_bot()
    bot.respond("When is the next tournament?")

    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"
