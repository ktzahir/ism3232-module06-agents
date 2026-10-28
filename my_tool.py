# my_tool.py
# Author: Kazi Zahir

# Creates a class that stores mock SSA soccer information.
class SoccerSchedule:
    """Store information about SSA soccer events."""

    #    __init__() — Runs when a new schedule object is created.
    def __init__(self):
        """Set up the pickup schedule and tournament information."""
        self.pickup_day = "Tuesday"
        self.pickup_time = "5 PM"
        self.pickup_location = "Fowler Fields"
        self.tournament_date = "November 23, 2026"

    #    get_pickup_schedule() — Returns the pickup day and time.
    def get_pickup_schedule(self):
        """Return the weekly pickup schedule."""
        return f"Pickup soccer is every {self.pickup_day} at {self.pickup_time}."

    def get_tournament_date(self):
        """Return the next tournament date."""
        return f"The next tournament is {self.tournament_date}."

    def get_pickup_location(self):
        """Return the pickup soccer location."""
        return f"Pickup soccer takes place at {self.pickup_location}."
