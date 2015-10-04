from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium_utils import *

from showdown_pokemon import ShowdownPokemon

from enum import Enum

#For associating players with their info
PLAYER_ELEMS = ['leftbar', 'rightbar']
ACTIVE_POKE_ELEMS = ['rstatbar', 'lstatbar']
class Player(Enum):
    me = 0
    op = 1

class ShowdownBattle(object):
    """docstring for ShowdownBattle"""

    #Elements
    root = None
    driver = None

    my_user = None
    op_user = None

    TOOLTIP_PATH = "//div[@id='tooltipwrapper']/div/div[@class='tooltip']"

    def __init__(self, driver, battle_room_elem):
        super(ShowdownBattle, self).__init__()
        self.driver = driver
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

    #----GAME STATUS
    #------------------------------------------------------------

    #----Symmetrical
    def get_team(self, player):
        team = []
        xpath = "//div[@class='{}']/div[@class='trainer']/div[@class='teamicons']//span"
        poke_elems = self.root.find_elements_by_xpath(xpath.format(PLAYER_ELEMS[player.value]))
        for poke_elem in poke_elems:
            team.append(ShowdownPokemon.from_team_icon(poke_elem))
        return team

    def get_active_pokemon(self, player):
        xpath = "//div[@class='statbar {}']/strong".format(ACTIVE_POKE_ELEMS[player.value])
        poke_elem = self.root.find_element_by_xpath(xpath)
        return ShowdownPokemon.from_team_icon(poke_elem)

    #----Unilateral
    def get_moves(self, player):
        xpath = "//div[@class='movemenu']/button"
        button_elems = self.root.find_elements_by_xpath(xpath)
        return [ShowdownMove.from_move_button(x) for x in button_elems]

    def get_my_full_team(self):
        xpath = "//div[@class='switchmenu']/button"
        poke_buttons = self.root.find_elements_by_xpath(xpath)
        pokemon = []
        for poke_button in poke_buttons:
            ActionChains(self.driver).move_to_element(poke_button).perform()
            tooltip = self.driver.find_element_by_xpath(self.TOOLTIP_PATH)
            pokemon.append(ShowdownPokemon.from_pop_up(poke_button, tooltip))

        return pokemon

    #----GAME ACTIONS
    #------------------------------------------------------------
    def switch_pokemon(self, poke):
        xpath = "//button[@name='chooseSwitch'][normalize-space(text())='{}']".format(poke['name'])
        poke_button = self.root.find_element_by_xpath(xpath)
        poke_button.click()

    def use_move(self, move):
        xpath = "//button[@name='chooseMove'][@data-move='{}']".format(move)
        move_button = self.root.find_element_by_xpath(xpath)
        move_button.click()

    def mega_evolve(self):
        xpath = ''

    def chat(self, text):
        xpath = "//form[@class='chatbox']/textarea[@placeholder='']"
        chat_form = self.root.find_element_by_xpath(xpath)
        chat_form.send_keys(text)
        chat_form.submit()
