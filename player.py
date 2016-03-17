import random
from validplays import *
from validstrategies import *

class Player:
    def __init__(self,name='Generic Player',history=[]):
        assert type(history) == list
        assert type(name) == str
        self.name = name
        self.history = history
        
    def strategy(self,opponent=None):
        return random.choice(VALID_PLAYS)

    def reset(self):
        '''Resets history
        '''
        self.history = []
        return

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
        
