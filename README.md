# Propositional_Logic_AI

The figure below shows a Land mine world containing two land mines. There is an agent in room [1,1]. The goal of the agent is to exit the Land mine world alive. The agent can
exit the Land mine world by reaching room [4,4]. The Land mine world may contain several landmines, but there will always be a safe path from [1,1] to the exit. The agent will be able to detect a land mine from the rooms adjacent to the room containing the
land mine. There will be three possible percepts: ’= 0’, ’= 1’ and ’> 1’. The percept ’= 1’ means that one of the adjacent rooms have a land mine. The percept ’> 1’ means
that two or more of the adjacent rooms have a land mine. Consider the figure shown below.

![Wumpus World](https://www.researchgate.net/figure/A-Typical-Wumpus-World_fig1_2430434)

If the agent is in room [2,1], then it will detect/perceive ’> 1’. If the agent is in room [1,2], then the percept will be ’= 1’. In room [1,3], the percept will be ’= 0’.

A python program has been written that uses propositional logic sentences to check which rooms are safe. The inference should be drawn using the SAT solver python-sat 1.Thelogical
agent can take four actions: Up, Down, Left and Right. These actions help the agent move from one room to an adjacent room. You may assume that there will always be a safe path that the agent can take to exit the Wumpus world. In other words, you can assume that the agent will not have to take a risk while navigating the minefield. Your goal is to make the agent move from [1,1] to [4,4] using minimum number of actions.
