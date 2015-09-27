from showdown_client import ShowdownClient
from showdown_battle import ShowdownBattle, Player

import time, json, code

def main():
    client = ShowdownClient()
    with open('config.json', 'r') as f:
        config = json.load(f)
    client.login(**config['login'])
    time.sleep(1)
    battle = client.challenge('chabons')
    team = battle.get_team(Player.me)
    #print(team)
    code.interact(local=locals())

if __name__ == '__main__':
    main()
