# AI Usage Documentation

## ISM 3232 - Module 10: OOP for Agents

I used ChatGPT to help develop and understand parts of my MatchDay SSA Soccer Assistant mini-project.

AI assistance included generating the initial SoccerSchedule and SoccerAssistant class definitions, explaining Python concepts such as classes, objects, methods, self, and composition, and helping troubleshoot errors.

I reviewed the code, added explanatory comments, tested the assistant manually, and ran pytest to verify its functionality.

All 18 automated tests passed.

## AI-Generated Class Code

The original AI-generated versions of the SoccerSchedule and SoccerAssistant classes are included below for transparency.

### Original AI-Generated SoccerSchedule Class
class SoccerSchedule:
    """Store information about SSA soccer events."""

    def __init__(self):
        """Set up the pickup schedule and tournament information."""
        self.pickup_day = "Tuesday"
        self.pickup_time = "5 PM"
        self.pickup_location = "Fowler Fields"
        self.tournament_date = "November 23, 2026"

    def get_pickup_schedule(self):
        """Return the weekly pickup schedule."""
        return f"Pickup soccer is every {self.pickup_day} at {self.pickup_time}."

    def get_tournament_date(self):
        """Return the next tournament date."""
        return f"The next tournament is {self.tournament_date}."
```