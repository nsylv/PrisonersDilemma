'''Player controlled by the computer

Holds all of the potential computer strategies,
and plays according to which one is selected.

Note: if adding a new strategy, make sure to update
the validstrategies.py to include it
'''
import random
from player import Player
from validplays import *
from validstrategies import *

class ComputerPlayer(Player):
    def __init__(self,name='Computer',history=[],strat=RANDOM):
        Player.__init__(self,name=name,history=history)
##        assert strat in VALID_STRATEGIES
        self.strat = strat

    def change_strat(self,new_strat):
##        assert new_strat in VALID_STRATEGIES
        self.strat = new_strat
        return

    def tit_for_tat(self,opponent):
        '''Play opponent's last move

        Defaults to SILENT (cooperating) if
        the opponent has no history
        '''
        if len(opponent.history) == 0:
            return SILENT
        return opponent.history[-1]

    def random(self,opponent):
        '''Play a random move
        '''
        return random.choice(VALID_PLAYS)

    def always_betray(self,opponent):
        '''Always betrays, no matter what
        '''
        return BETRAY

    def always_silent(self,opponent):
        '''Always silent, no matter what
        '''
        return SILENT

    def strategy(self,opponent):
        '''Plays according to the selected strategy

        If no strategy (or an invalid strategy) is
        selected, it just plays with random strategy
        '''
        if self.strat == TITFORTAT:
            return self.tit_for_tat(opponent)
        elif self.strat == RANDOM:
            return self.random(opponent)
        elif self.strat == ALWAYSBETRAY:
            return self.always_betray(opponent)
        elif self.strat == ALWAYSSILENT:
            return self.always_silent(opponent)
        all_strats = [self.tit_for_tat,self.random,self.always_betray,self.always_silent]
        return random.choice(all_strats)(opponent) #invalid strat selected, choose to play with random strat (NOTE: this case should never happen, but you never know I guess)
        
