from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from showdown_battle import ShowdownBattle

import time, json

class ShowdownClient(object):
    """docstring for ShowdownCLient"""

    #Constants
    SERVER_URL = "http://play.pokemonshowdown.com/"

    #Field declaration
    driver = None

    username = None

    def __init__(self):
        super(ShowdownClient, self).__init__()
        self.driver = webdriver.Firefox()
        #self.driver.firefox_profile.set_preference("media.volume_scale", "0.0")
        self.driver.get(self.SERVER_URL)

    def __del__(self):
        self.driver.close()

    def login(self, username='', password=''):
        #Open the login menu
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME,'login'))
        )
        login_button.click()

        username_input = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys(username)
        username_input.submit()

        password_input = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys(password)
        password_input.submit()

        self.username = username

    def ladder(self, format=None):
        pass

    def challenge(self, username, format=None, timeout=30):
        """
        Returns the battle object for this match, or false if it is rejected
        """
        find_user_button = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//button[@name='finduser']"))
        )
        find_user_button.click()

        username_input = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='data']"))
        )
        username_input.send_keys(username)
        username_input.submit()

        challenge_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@name='challenge']"))
        )
        challenge_button.click()

        #TODO:Select format

        make_challenge_button = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//button[@name='makeChallenge']"))
        )
        make_challenge_button.click()

        try:
            battle_obj = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'ps-room')]/div[@class='battle']"))
            )
            battle_room = battle_obj.find_element_by_xpath('..')
            return ShowdownBattle(battle_room)
        except TimeoutException:
            print("Challenge timed out")
            return None

def main():
    client = ShowdownClient()
    with open('config.json', 'r') as f:
        config = json.load(f)
    client.login(**config['login'])
    time.sleep(2)
    print(client.challenge('chabons'))


if __name__ == '__main__':
    main()
