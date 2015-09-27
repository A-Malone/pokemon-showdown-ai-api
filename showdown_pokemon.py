
class ShowdownPokemon(object):
    """A representation of a pokemon obtained from PS"""

    #CONSTANTS
    STATES = ['active','fainted']

    #Fields
    name = None
    active = False
    fainted = False

    def __init__(self, name_string, active=False, fainted=False):
        super(ShowdownPokemon, self).__init__()

        #Parse any state info included in the name
        for state in self.STATES:
            if(name_string.endswith(" ({})".format(state))):
                self.name = name_string.split(' ')[0]
                setattr(self, state, True)
                break
        else:
            self.name = name_string
            self.active = active
            self.fainted = fainted

    def __str__(self):
        return "ShowdownPokemon: {}".format(self.name)
