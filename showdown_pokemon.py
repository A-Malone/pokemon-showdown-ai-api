import re

#----UTILITIES
#------------------------------------------------------------
def recursive_check(schema, data):
    if(type(data)==dict==type(schema)):
        for k in schema:
            if(data.get(k,  False)):
                recursive_check(schema[k], data[k])
    elif(type(data)==list==type(schema)):
        if(len(data)>0):
            recursive_check(schema[0], data[0])
    elif(type(data)==type(schema)):
        pass
    else:
        raise ValueError("Schema violation: {} should be {}".format(data, schema))


def schema_validated(func):
    def inner(f_cls, *args):
        ret_val = func(f_cls, *args)
        recursive_check(f_cls.schema, ret_val)
        return ret_val
    return inner

#----CLASSES
#------------------------------------------------------------
class ShowdownPokemon(object):
    """A class to get dict representations of pokemon from PS"""
    schema = {
        'name':'',
        'hp':0,
        'maxhp':0,
        'ability':'',
        'item':'',
        'stats':[0],
        'state':'',
        'status':['']
    }
    STATES = ['active', 'fainted']
    STATUSES = []

    @classmethod
    @schema_validated
    def from_team_icon(cls, poke_elem):
        root = {}
        name_string = poke_elem.get_attribute('title')
        #Parse any state info included in the name
        for state in cls.STATES:
            if(name_string.endswith(" ({})".format(state))):
                root['name'] = name_string.split(' ')[0]
                root['status'].append(state)
                return root

    @classmethod
    @schema_validated
    def from_pop_up(cls, button_object, pop_up):
        root = {}

        #Parse data on the button
        data = button_object.get_attribute('value').split(',')
        root['name'] = data[0]
        if(len(data) > 1):
            root['state'] = data[1]

        #Parse the pop-up
        sections = pop_up.find_elements_by_tag_name('p')

        #Parse status
        root['stats'] = []
        statuses = sections[0].find_elements_by_tag_name('span')
        for status in statuses:
            root['stats'].append(status.text)

        #Parse HP
        hp_string = sections[0].text
        hp_data = re.findall(r'\d+/(?:\d+|undefined)', hp_string)[0].split('/')
        root['hp'] = int(hp_data[0])
        root['max_hp'] = int(hp_data[1])

        ability_string = sections[1].text
        root['ability'] = ability_string.split(': ')[-1]

        item_string = sections[2].text
        root['item'] = item_string.split(': ')[-1]

        stats_string = sections[3].text
        root['stats'] = [int(x) for x in re.findall(stats_string, r'\d+')]

        return root

class ShowdownMove(object):
    """A class to get dict representations of move from PS"""
    schema = {
        'name':'',
        'type':'',
        'pp':[0,0]
    }
    @classmethod
    @schema_validated
    def from_move_button(cls, move_button):
        root = {}
        root['name'] = move_button.text
        root['type'] = move_button.find_element_by_class('type').text
        root['pp'] = [int(x) for x in move_button.find_element_by_class('pp').text.split('/')]

#Simple test
def main():
    data = {'name':'Charizard'}
    recursive_check(ShowdownPokemon.schema, data)

if __name__ == '__main__':
    main()
