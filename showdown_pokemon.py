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
    def inner(*args):
        ret_val = func(*args)
        recursive_check(f_cls.schema, ret_val)
    return inner

#----CLASSES
#------------------------------------------------------------
class ShowdownPokemon(object):
    """A class to get dict representations of pokemon from PS"""
    schema = {
        'name':''
    }
    STATES = ['active', 'fainted']

    @classmethod
    @schema_validated
    def from_team_icon(cls, poke_elem):
        root = {}
        name_string = poke_elem.get_attribute('title')
        #Parse any state info included in the name
        for state in cls.STATES:
            if(name_string.endswith(" ({})".format(state))):
                root['name'] = name_string.split(' ')[0]
                root[state] = True
                return root

    @classmethod
    @schema_validated
    def from_pop_up(cls, pop_up):
        root = {}
        name_string = poke_elem.text
        #Parse any state info included in the name
        for state in cls.STATES:
            if(name_string.endswith(" ({})".format(state))):
                root['name'] = name_string.split(' ')[0]
                root[state] = True
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
