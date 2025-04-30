import random
from typing import Dict, Any

class GameManager:
    def __init__(self):
        self.players: Dict[int, Dict[str, Any]] = {}
        self.current_game = None
        self.games = {
            'never_have_i_ever': {
                'questions': [
                    # ... (same questions as before)
                ],
                'description': "Players admit things they've never done."
            },
            'truth_or_drink': {
                'questions': [
                    # ... (same questions as before)
                ],
                'description': "Answer truthfully or take a drink!"
            },
            'kings_cup': {
                'cards': {
                    # ... (same cards as before)
                },
                'description': "Virtual Kings Cup game"
            }
        }

    # ... (all the game methods from previous example)
    # Note: Include all the methods shown in the previous games.py example
