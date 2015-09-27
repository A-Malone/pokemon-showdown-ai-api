from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Move(object):
    """docstring for Move"""
    def __init__(self, name):
        super(Move, self).__init__()
        self.name = name


class ShowdownBattle(object):
    """docstring for ShowdownBattle"""

    battle_room_elem = None

    my_user = None
    op_user = None

    def __init__(self, battle_room_elem):
        super(ShowdownBattle, self).__init__()
        self.battle_room_elem = battle_room_elem

        my_trainer_elem = WebDriverWait(self.battle_room_elem, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='leftbar']/div[@class='trainer']"))
        )
        self.my_user = my_trainer_elem.find_element_by_tag_name('strong').text

        op_trainer_elem = WebDriverWait(self.battle_room_elem, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='rightbar']/div[@class='trainer']"))
        )
        self.op_user = my_trainer_elem.find_element_by_tag_name('strong').text

    def __str__(self):
        print("Battle: {} vs {}".format(my_user, op_user))

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
