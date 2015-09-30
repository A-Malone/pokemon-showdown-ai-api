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
    if('battle'):
        team = battle.get_team(Player.me)
        #Start a terminal
        terminal = code.InteractiveConsole(locals=locals())
        terminal.push('from showdown_client import ShowdownClient')
        terminal.push('from showdown_battle import ShowdownBattle, Player')
        terminal.interact()

if __name__ == '__main__':
    main()
