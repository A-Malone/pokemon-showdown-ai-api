#TODO: Write decorator validator for classes

class ShowdownPokemon(object):
    """A class to get dict representations of pokemon from PS"""
    STATES = ['active', 'fainted']
    @classmethod
    def from_team_icon(cls, poke_elem):
        root = {}
        name_string = poke_elem.get_attribute('title')
        #Parse any state info included in the name
        for state in cls.STATES:
            if(name_string.endswith(" ({})".format(state))):
                root['name'] = name_string.split(' ')[0]
                root[state] = True
                return root

class ShowdownMove(object):
    """A class to get dict representations of move from PS"""
    STATES = ['active', 'fainted']
    @classmethod
    def from_move_button(cls, move_button):
        root = {}
        root['name'] = move_button.text
        root['type'] = move_button.find_element_by_class('type').text
        root['pp'] = move_button.find_element_by_class('pp').text.split('/')
