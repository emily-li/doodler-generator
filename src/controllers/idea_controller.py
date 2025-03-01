import random
from models.idea import Idea


class IdeaController:
    ideas: list[str]

    def __init__(self):
        self.ideas = [
            "a cat wearing a hat",
            "a futuristic city",
            "a doodle of a dragon",
            "a cozy coffee shop",
            "a whimsical treehouse",
            "a dog with a frog",
            "a fish with a dish",
            "a bear with a pear",
            "a fox wearing socks",
            "a mouse with a house",
        ]

    def get_idea(self) -> Idea:
        return Idea(random.choice(self.ideas))
