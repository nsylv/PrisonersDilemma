''' Play the cannonical prisoner's dilemma

\tYou and the other player have been imprisoned for
petty theft of a gas station.  However, after you fled the
scene, a huge fire erupted.  The police have ample evidence
that you two were behind the theft, but they also have
suspicions that you two are behind the arson as well.
Since arson is a much worse crime, it also comes with a
higher prison sentence.  Unfortunately, the cops don't
have enough evidence to convict you on the higher crime, so
they want a confession.
\tYou and the other player are put in separate rooms.
The police will offer each of you a chance to betray the
other.  If you betray your partner but they decide to
remain silent, you will be pardoned for your minor crime
(get 0 years of jail sentence) and your partner will have
to serve 3 years.  However, if you betray your partner and
they betray you, you each receive 2 years of jail time.
If you both remain silent, both of you will serve a 1
year sentence.

'''

import random
import itertools #used for testing strats
from player import Player
from humanplayer import HumanPlayer
from computerplayer import ComputerPlayer

from util import *
from outcomes import *
from validstrategies import *
from validplays import *

from printtable import print_table

class Game:
    def __init__(self):
        pass

    def get_player(self,player_num):
        h_or_c = None
        while (h_or_c != 'h') and (h_or_c != 'c'):
            h_or_c = raw_input('Is player {} (h)uman or (c)omputer? '.format(player_num))
            if (h_or_c != 'h') and (h_or_c != 'c'):
                cls()
                print 'Invalid selection, must be "{}" or "{}"'.format('h','c')
        if h_or_c == 'h': #human player
            name = raw_input('What is your name? ')
            p = HumanPlayer(name)
        else: #computer player
            strat_string = ''
            for i in range(len(VALID_STRATEGIES)):
                strat_string += '\t{}) {}\n'.format(i,VALID_STRATEGIES[i])
            strat_num = len(VALID_STRATEGIES) + 1
            while (strat_num > len(VALID_STRATEGIES)):
                strat_num = input('Choose a strat:\n'+strat_string+'\t{}) Any\n'.format(i+1))
                if strat_num > len(VALID_STRATEGIES):
                    cls()
                    print 'Invalid strat, must be between 0 and {}'.format(len(VALID_STRATEGIES))
            #Get strat
            if strat_num < len(VALID_STRATEGIES):
                strat = VALID_STRATEGIES[strat_num]
            elif strat_num == len(VALID_STRATEGIES):
                strat = random.choice(VALID_STRATEGIES)
            #Make player with strat
            p = ComputerPlayer(name='Computer_{}'.format(player_num),strat=strat)
        return p

    def is_done(self):
        valid = ['y','n']
        play_again = None
        while play_again not in valid:
            play_again = raw_input('Play again? (y/n) ')
            if play_again not in valid:
                cls()
                print 'Invalid selection, please select "{}" or "{}"'.format('y','n')
        return play_again == 'n'
        
    def play(self,do_cls=True):
        '''Get the two players' sentences, add their decisions to their histories

        Output:
            (p1_sentence,p2_sentence) ~ (VALID_PLAY,VALID_PLAY) ~ the decisions of each of the players
        '''
        if do_cls:
            cls()
        #Get the two players' decisions
        p1_decision = self.p1.strategy(self.p2)
        if do_cls:
            cls() #clear screen after decision so p2 can't see p1's decision
        p2_decision = self.p2.strategy(self.p1)
        if do_cls:
            cls() #clear screen after decision so p1 can't see p2's decision
        #Add their decisions to their histories
        self.p1.history.append(p1_decision)
        self.p2.history.append(p2_decision)
        if do_cls:
            print '{} chose to {}, {} chose to {}'.format(self.p1.name,p1_decision,self.p2.name,p2_decision)
        #Get sentences from their decisions
        p1_sentence,p2_sentence = self.calculate_sentences(p1_decision,p2_decision)
        return p1_sentence,p2_sentence

    def calculate_sentences(self,p1_decision,p2_decision):
        '''Gives the sentences of the two players based
            upon their decisions
            
            Cases:
                p1 betray, p2 betray
                p1 betray, p2 silent
                p1 silent, p2 betray
                p1 silent, p2 silent

            Inputs:
                p1_decision - BETRAY/SILENT
                p2_decision - BETRAY/SILENT
            Output:
                (p1_sentence,p2_sentence) - (Integer,Integer)
        '''
        p1_sentence = -1
        p2_sentence = -1
        if p1_decision == BETRAY:
            if p2_decision == BETRAY:
                p1_sentence = R
                p2_sentence = R
            elif p2_decision == SILENT:
                p1_sentence = S
                p2_sentence = T
        elif p1_decision == SILENT:
            if p2_decision == BETRAY:
                p1_sentence = T
                p2_sentence = S
            elif p2_decision == SILENT:
                p1_sentence = P
                p2_sentence = P
        return (p1_sentence,p2_sentence)

    def print_results(self,p1,p1_sentence,p2,p2_sentence):
        print '{} got a {} year sentence, {} got a {} year sentence'.format(p1.name,p1_sentence,p2.name,p2_sentence)
        return

    def main(self,p1=None,p2=None):
        cls()
        print "Welcome to Prisoner's Dilemma!"
        if not p1:
            self.p1 = self.get_player(1)
        if not p2:
            self.p2 = self.get_player(2)
        cls()
        done = False
        while not done:
            p1_sentence,p2_sentence = self.play()
            self.print_results(self.p1,p1_sentence,self.p2,p2_sentence)
            done = self.is_done()
            cls()
        print 'Thank you for playing Prisoner\'s Dilemma!'
        return

    def test_strats(self):
        '''Tests all of the strats against each other
        '''
        NUMBER_OF_TRIALS = 100000
        results = {}
        old_strat_combos = [x for x in itertools.product(VALID_STRATEGIES,repeat=2)]
        strat_combos = []
        for combo in old_strat_combos:
            if combo[::-1] not in strat_combos:
                strat_combos.append(combo)
        for strat1,strat2 in strat_combos:
            self.p1 = ComputerPlayer(name='Computer1',strat=strat1)
            self.p2 = ComputerPlayer(name='Computer2',strat=strat2)
            results[(strat1,strat2)] = {'number of trials':NUMBER_OF_TRIALS,'p1 results':[],'p2 results':[],'number of best outcomes':0,'number of p1 worst outcomes':0,'number of p2 worst outcomes':0,'number of average outcomes':0,'number of bad outcomes':0}
            #Get results
            for i in range(NUMBER_OF_TRIALS):
                key = (strat1,strat2)
                p1_sentence,p2_sentence = self.play(do_cls=False)
                results[key]['p1 results'].append((p1_sentence))
                results[key]['p2 results'].append((p2_sentence))
                if p1_sentence == P and p2_sentence == P: #both players stay silent
                    results[key]['number of best outcomes'] += 1
                if p1_sentence == R and p2_sentence == R: #both players defected
                    results[key]['number of average outcomes'] += 1
                if p1_sentence == T:
                    results[key]['number of p1 worst outcomes'] += 1
                    results[key]['number of bad outcomes'] += 1
                if p2_sentence == T:
                    results[key]['number of p2 worst outcomes'] += 1
                    results[key]['number of bad outcomes'] += 1

        #Process Results        
        for s1,s2 in results.keys():
            key = (s1,s2)
            #get average p1 sentence
            results[key]['p1 average sentence'] = sum(results[key]['p1 results'])/float(len(results[key]['p1 results']))
            #get average p2 sentence
            results[key]['p2 average sentence'] = sum(results[key]['p2 results'])/float(len(results[key]['p2 results']))

        #Get the sentence lengths for each strat
        sentences_for_strat = {} #{strat:[your_total_sentence_for_using_strat,number_of_trials,other_players_total_sentence_for_competing_against_strat}
        for strat in VALID_STRATEGIES:
            your_total_sentence = 0
            trials = 0
            other_total_sentence = 0
            for s1,s2 in results.keys():
                key = (s1,s2)
                if s1 != s2:
                    if s1 == strat:
                        your_total_sentence += sum(results[key]['p1 results'])
                        other_total_sentence += sum(results[key]['p2 results'])
                        trials += results[key]['number of trials']
                    elif s2 == strat:
                        your_total_sentence += sum(results[key]['p2 results'])
                        other_total_sentence += sum(results[key]['p1 results'])
                        trials += results[key]['number of trials']
            both_same = (sum(results[(strat,strat)]['p1 results'])+sum(results[(strat,strat)]['p2 results']))/2 #take the average of p1 and p2 results, since both are using the same strat
            your_total_sentence += both_same
            other_total_sentence += both_same
            trials += results[(strat,strat)]['number of trials']
            sentences_for_strat[strat] = [your_total_sentence,trials,other_total_sentence]

        #Print Results (using print_table)
        print 'Results of different strategy combinations'
        trials = NUMBER_OF_TRIALS
        headers = ['Strat1','Strat2','P1 Avg','P2 Avg','Best/Trials','Avg/Trials','Bad/Trials','P1 Bad/Trials','P2 Bad/Trials']
        rows = [[strat1,strat2,results[strat1,strat2]['p1 average sentence'],results[strat1,strat2]['p2 average sentence'],'{}/{}'.format(results[strat1,strat2]['number of best outcomes'],trials),'{}/{}'.format(results[strat1,strat2]['number of average outcomes'],trials),'{}/{}'.format(results[strat1,strat2]['number of bad outcomes'],trials),'{}/{}'.format(results[strat1,strat2]['number of p1 worst outcomes'],trials),'{}/{}'.format(results[strat1,strat2]['number of p2 worst outcomes'],trials)] for strat1,strat2 in results.keys()]
        
##        #Sort by strat 1
##        print 'Sorted by P1's Strategy:'
##        rows = sorted(rows,key=lambda x: x[0])
##        
##        #Sort by strat 2
##        print 'Sorted by P2's Strategy:'
##        rows = sorted(rows,key=lambda x: x[1])
##        
##        #Sort by p1 avg
##        print 'Sorted by P1 Average Sentence:'
##        rows = sorted(rows,key=lambda x: x[2],reverse=True)
##        
##        #Sort by p2 avg
##        print 'Sorted by P2 Average Sentence:'
##        rows = sorted(rows,key=lambda x: x[3],reverse=True)
##        
##        #Sort by best
        print 'Sorted by Number of Best Outcomes:'
        rows = sorted(rows,key=lambda x: int(x[4][:x[4].index('/')]),reverse=True)
##        
##        #Sort by avg
##        print 'Sorted by Number of Average Outcomes'
##        rows = sorted(rows,key=lambda x: int(x[5][:x[5].index('/')]),reverse=True)
##        
##        #Sort by bad
##        print 'Sorted by Number of Bad Outcomes'
##        rows = sorted(rows,key=lambda x: int(x[6][:x[6].index('/')]),reverse=True)
##        
##        #Sort by p1 bad
##        print 'Sorted by Number of Bad Outcomes for P1'
##        rows = sorted(rows,key=lambda x: int(x[7][:x[7].index('/')]),reverse=True)
##        
##        #Sort by p2 bad
##        print 'Sorted by Number of Bad Outcomes for P2'
##        rows = sorted(rows,key=lambda x: int(x[8][:x[8].index('/')]),reverse=True)
        
        print_table(headers,rows)


        print '\n\n'
        print 'Sentence lengths for playing with and against certain strategies'
        headers = ['Strat','Average for Using','Total Sent/Trials','Average for Against','Total Sent/Trials','Total Average']
        rows = [[strat,float(sentences_for_strat[strat][0])/sentences_for_strat[strat][1],'{}/{}'.format(sentences_for_strat[strat][0],sentences_for_strat[strat][1]),float(sentences_for_strat[strat][2])/sentences_for_strat[strat][1],'{}/{}'.format(sentences_for_strat[strat][2],sentences_for_strat[strat][1]),(sentences_for_strat[strat][0]+sentences_for_strat[strat][2])/(sentences_for_strat[strat][1] * 2.)] for strat in sentences_for_strat.keys()]
        print_table(headers,rows)
        return results
            
        
            

#If run, do the main loop
if __name__ == '__main__':
    g = Game()
##    results = g.test_strats()
    g.main()
