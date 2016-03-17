from player import Player

from validplays import *
from validstrategies import *
from util import *

class HumanPlayer(Player):
    def strategy(self,opponent=None):
        choice = None
        while choice not in VALID_PLAYS:
            choice = raw_input('{}, are you going to (b)etray or remain (s)ilent? '.format(self.name))
            if (choice not in VALID_PLAYS):
                cls()
                print 'Invalid choice, please choose "{}" or "{}"'.format(BETRAY,SILENT)
        return choice
    
            
