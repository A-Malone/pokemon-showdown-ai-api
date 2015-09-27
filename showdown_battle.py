from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from enum import Enum

#For associating players with their info
PLAYER_ELEMS = ['leftbar', 'rightbar']
class Player(Enum):
    me = 0
    op = 1

class ShowdownBattle(object):
    """docstring for ShowdownBattle"""

    root = None

    my_user = None
    op_user = None

    def __init__(self, battle_room_elem):
        super(ShowdownBattle, self).__init__()
        self.root = battle_room_elem

        self.my_user = self.get_username(Player.me)
        self.op_user = self.get_username(Player.op)

    def __str__(self):
        return "Battle: {} vs {}".format(self.my_user, self.op_user)

    #Static infor methods
    def get_username(self, player):
        trainer_elem = WebDriverWait(self.root, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='{}']/div[@class='trainer']".format(PLAYER_ELEMS[player.value])))
        )
        return trainer_elem.find_element_by_tag_name('strong').text

    #Game status methods
    def get_team(self, player):
        team = []
        xpath = "//div[@class='{}']/div[@class='trainer']/div[@class='teamicons']//span"
        poke_elems = self.root.find_elements_by_xpath(xpath.format(PLAYER_ELEMS[player.value]))
        for poke_elem in poke_elems:
            team.append(poke_elem.get_attribute('title').replace(' (active))',''))

    def get_active_pokemon(self, player):
        pass

    #Actions
    def switch_pokemon(self, poke):
        pass

    def use_move(self, move):
        pass
