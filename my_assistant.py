# my_assistant.py
# Author: Kazi Zahir


class SoccerAssistant:
    """A mock soccer assistant that answers SSA event questions."""

    # Sets up the assistant when it’s created.
    # self.schedule_tool Connects the assistant to the soccer schedule tool
    def __init__(self, name, schedule_tool):
        self.name = name
        self.schedule_tool = schedule_tool
        self.history = []

    # Receives a message, generates a reply, and saves both messages.
    def respond(self, user_message):
        self.history.append({"role": "user", "content": user_message})

        reply = self.choose_reply(user_message)

        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a response using keywords."""
        text = user_message.lower()

        if "change" in text and "team" in text:
            return "Team changes require approval. Please contact an SSA organizer for assistance."

        if "tournament" in text:
            return self.schedule_tool.get_tournament_date()

        if "where" in text or "location" in text:
            return self.schedule_tool.get_pickup_location()

        if "pickup" in text or "pick up" in text:
            return self.schedule_tool.get_pickup_schedule()

        return "I'm not sure how to help with that. I can answer questions about pickup soccer and tournaments."
