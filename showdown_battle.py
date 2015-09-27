from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Pokemon(object):
    """docstring for Pokemon"""

    #Stats
    health_pct = 1.0

    #Lists with ordering:
    #   Atk/Def/Spa/Spd/Spe
    stats = None
    max_stats = None
    min_stats = None
    boosts = None

    #Status effects
    status = {}

    def __init__(self, name):
        super(Pokemon, self).__init__()
        self.name = name

    def lookup_from_db(self):
        pass

class Move(object):
    """docstring for Move"""
    def __init__(self, name):
        super(Move, self).__init__()
        self.name = name


class ShowdownBattle(object):
    """docstring for ShowdownBattle"""

    battle_room_elem = None

    def __init__(self, battle_room_elem):
        super(ShowdownBattle, self).__init__()
        self.battle_room_elem = battle_room_elem

    #Game status methods
    def get_teams(self):
        pass

    def get_my_active_pokemon(self):
        pass

    def get_oponent_active_pokemon(self):
        pass

    #Actions
    def switch_pokemon(self, poke):
        pass

    def use_move(self, move):
        pass
