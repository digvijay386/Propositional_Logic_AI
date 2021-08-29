# Propositional_Logic_AI

The figure below shows a Land mine world containing two land mines. There is an agent in room [1,1]. The goal of the agent is to exit the Land mine world alive. The agent can
exit the Land mine world by reaching room [4,4]. The Land mine world may contain several landmines, but there will always be a safe path from [1,1] to the exit. The agent will be able to detect a land mine from the rooms adjacent to the room containing the
land mine. There will be three possible percepts: ’= 0’, ’= 1’ and ’> 1’. The percept ’= 1’ means that one of the adjacent rooms have a land mine. The percept ’> 1’ means
that two or more of the adjacent rooms have a land mine. Consider the figure shown below.

![Wumpus World](https://www.researchgate.net/figure/A-Typical-Wumpus-World_fig1_2430434)

If the agent is in room [2,1], then it will detect/perceive ’> 1’. If the agent is in room [1,2], then the percept will be ’= 1’. In room [1,3], the percept will be ’= 0’.
