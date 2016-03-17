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

