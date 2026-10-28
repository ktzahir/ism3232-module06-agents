# my_main.py
# Author: Kazi Zahir

from my_assistant import SoccerAssistant
from my_tool import SoccerSchedule

schedule_tool = SoccerSchedule()
bot = SoccerAssistant("MatchDay", schedule_tool)

print("Welcome to the SSA Soccer Assistant!")
print("Type 'quit' to exit.")

while True:
    message = input("You: ")

    if message.lower() == "quit":
        break

    print(f"MatchDay: {bot.respond(message)}")
