# PrisonersDilemma
My implementation of the prisoner's dilemma program in python

##Quickstart
To play the game, run the following in a terminal window: <code>python main.py</code>

##Background
The prisoner's dilemma is a simple game originally devised by Merrill Flood and Melvin Dresher working at RAND in 1950.  The game was formalized by Albert W. Tucker and presented with the following story:
>Two members of a criminal gang are arrested and imprisoned. Each prisoner is in solitary confinement with no means of communicating with the other. The prosecutors lack sufficient evidence to convict the pair on the principal charge. They hope to get both sentenced to a year in prison on a lesser charge. Simultaneously, the prosecutors offer each prisoner a bargain. Each prisoner is given the opportunity either to: betray the other by testifying that the other committed the crime, or to cooperate with the other by remaining silent. The offer is:
>* If A and B each betray the other, each of them serves 2 years in prison
>* If A betrays B but B remains silent, A will be set free and B will serve 3 years in prison (and vice versa)
>* If A and B both remain silent, both of them will only serve 1 year in prison (on the lesser charge)

> -- <cite>Wikipedia</cite>

The generalized form of the possible outcomes is as follows (where `T > P > R > S`):

|           | Silent  | Betrays |
|:---------:|:-------:|:-------:|
|**Silent** |  R,R    |   S,T   |
|**Betrays**|  T,S    |   P,P   |

In the Wikipedia example, `T = 3, P = 2, R = 1, and S = 0`.

##Testing Strategies
There are several strategies that can be employed while playing this game.  In [computerplayer.py](computerplayer.py) you can see their logic.  Here is a brief summary:
* random ~ randomly selects to betray or stay silent
* tit for tat ~ responds with the opponent's last move (starts off by staying silent)
* always silent ~ always stays silent
* always betray ~ always betrays

I compared each of these strategies, finding out (using `T = 3, P = 2, R = 1, and S = 0`):
* P1 Avg ~ average sentence term for the first player (using Strat1)
* P2 Avg ~ average sentence term for the second player (using Strat2)
* Best ~ number of cases where the best-case scenario (both players stayed silent) was achieved
* Avg ~ number of cases where the average-case scenario (both players betrayed each other) was achieved
* Bad ~ number of cases where the worst-case scenario (one player gets maximum prison time) was achieved
* P1 Bad ~ number of cases where first player got maximum prison sentence
* P2 Bad ~ number of cases where second player got maximum prison sentence

###Strategies results (sorted by number of best-case outcomes) 

|Strat1       | Strat2       | P1 Avg  | P2 Avg  | Best/Trials   | Avg/Trials    | Bad/Trials    | P1 Bad/Trials | P2 Bad/Trials |
|:------------|:-------------|--------:|--------:|--------------:|--------------:|--------------:|--------------:|--------------:|
|AlwaysSilent | AlwaysSilent | 1.0     | 1.0     | 100000/100000 | 0/100000      | 0/100000      | 0/100000      | 0/100000      |
|TitForTat    | TitForTat    | 1.0     | 1.0     | 100000/100000 | 0/100000      | 0/100000      | 0/100000      | 0/100000      |
|TitForTat    | AlwaysSilent | 0.99999 | 1.00002 | 99999/100000  | 0/100000      | 1/100000      | 0/100000      | 1/100000      |
|random       | AlwaysSilent | 0.49817 | 2.00366 | 49817/100000  | 0/100000      | 50183/100000  | 0/100000      | 50183/100000  |
|TitForTat    | random       | 1.49876 | 1.49876 | 25013/100000  | 24765/100000  | 50222/100000  | 25111/100000  | 25111/100000  |
|random       | random       | 1.49764 | 1.50586 | 24842/100000  | 25192/100000  | 49966/100000  | 24846/100000  | 25120/100000  |
|AlwaysBetray | AlwaysBetray | 2.0     | 2.0     | 0/100000      | 100000/100000 | 0/100000      | 0/100000      | 0/100000      |
|random       | AlwaysBetray | 2.50002 | 0.99996 | 0/100000      | 49998/100000  | 50002/100000  | 50002/100000  | 0/100000      |
|TitForTat    | AlwaysBetray | 2.00001 | 1.99998 | 0/100000      | 99999/100000  | 1/100000      | 1/100000      | 0/100000      |
|AlwaysBetray | AlwaysSilent | 0.0     | 3.0     | 0/100000      | 0/100000      | 100000/100000 | 0/100000      | 100000/100000 |

Additionally, I looked at what using different strategies looked like without factoring in what the second strategy was.  In this analysis, I computed (using `T = 3, P = 2, R = 1, and S = 0`):
* Average for Using ~ average sentence term for using the given strategy
* Average for Against ~ average sentence term for playing against the given strategy
* Total Average ~ average sentence of the players for at least one of them using the given strategy
* Cum Average ~ average total sentence of the two players for at least one of them using the given strategy (i.e. average p1_sentence + p2_sentence)

###Strategies results (sorted by total average)
|Strat        | Average for Using | Average for Against | Total Average | Cum Average |
|------------:|------------------:|--------------------:|--------------:|------------:|
|AlwaysSilent | 1.74806           | 0.62597             | 1.187015      | 2.37403     |
|TitForTat    | 1.37466           | 1.37466             | 1.37466       | 2.74932     |
|random       | 1.499935          | 1.498135            | 1.499035      | 2.99807     |
|AlwaysBetray | 1.25074           | 2.37463             | 1.812685      | 3.62537     |
