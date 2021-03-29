from Agent import * 
from pysat.solvers import Glucose3
from queue import Queue
import copy

kb=Glucose3()
a=[1,2,3,4]
locations=[(i,j) for i in a for j in a]
locations.sort()

#mostly not needed
end={}
ptr=1
for location in locations:
	end[location]=ptr
	ptr+=1

#to check if stuff is visted or not
#positive=>visited
#negative=>not visited

#-------------1 to 16, both inclusive----------
x=[i for i in range(1,17)]
visited={}
ptr=0
#no change needed for the translation problem
for location in locations:
	visited[location]=(-1)*x[ptr]
	ptr+=1

#to check if a thing has mine or not
#positive=> has mine
#negative=> does'nt have mine

#-------------101 to 116, both inclusive----------
x=[i+100 for i in x]
hasMine={}
ptr=0
#no change needed for the translation problem

for location in locations:
	hasMine[location]=x[ptr]
	ptr+=1

hasMine[(1,1)]=101
hasMine[(4,4)]=116
#-------------201 to 216, both inclusive----------
x=[i+100 for i in x]
perceivedZero={}
ptr=0
#no change needed for the translation problem

for location in locations:
	perceivedZero[location]=x[ptr]
	ptr+=1


#add to this as and when required
#-------------301 to 316, both inclusive----------
x=[i+100 for i in x]
perceivedOne={}
ptr=0
#no change needed for the translation problem

for location in locations:
	perceivedOne[location]=x[ptr]
	ptr+=1
#-------------401 to 416, both inclusive----------
x=[i+100 for i in x]
perceivedMore={}
ptr=0
#no change needed for the translation problem

for location in locations:
	perceivedMore[location]=x[ptr]
	ptr+=1
#-------------501 to 516, both inclusive----------
x=[i+100 for i in x]
canMoveUp={}
ptr=0
#no change needed for the translation problem

for location in locations:
	if(location[1]==4):
		canMoveUp[location]=(-1)*x[ptr]
	else:
		canMoveUp[location]=x[ptr]
	ptr+=1


#-------------601 to 616, both inclusive----------
x=[i+100 for i in x]
canMoveDown={}
ptr=0
#no change needed for the translation problem

for location in locations:
	if(location[1]==1):
		canMoveDown[location]=(-1)*x[ptr]
	else:
		canMoveDown[location]=x[ptr]
	ptr+=1




#-------------701 to 716, both inclusive----------
x=[i+100 for i in x]
canMoveRight={}
ptr=0
#no change needed for the translation problem

for location in locations:
	if(location[0]==4):
		canMoveRight[location]=(-1)*x[ptr]
	else:
		canMoveRight[location]=x[ptr]
	ptr+=1


#-------------801 to 816, both inclusive----------
x=[i+100 for i in x]
canMoveLeft={}
ptr=0
#no change needed for the translation problem

for location in locations:
	if(location[0]==1):
		canMoveLeft[location]=(-1)*x[ptr]
	else:
		canMoveLeft[location]=x[ptr]
	ptr+=1


#almost done
#i'm guessing is fine
def add_clauses_more_3(t):
	if(t[0]==4):
		
		kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*perceivedMore[t],(1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])

		kb.add_clause([(-1)*perceivedMore[t],(1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*perceivedMore[t],(1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*perceivedMore[t],(1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*perceivedMore[t],(-1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])




	if(t[0]==1):
		kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])

		kb.add_clause([(-1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])

	if(t[1]==4):
		kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]-1)]])

		kb.add_clause([(-1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]-1)]])

	if(t[1]==1):
		kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)]])

		kb.add_clause([(-1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(-1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(-1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(-1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)]])

#almost done
#i'm guessing is fine

def add_clauses_one_3(t):
  if(t[0]==4):
  	print("xcfghujio")
  	kb.add_clause([(1)*perceivedOne[t],(-1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])
  	kb.add_clause([(1)*perceivedOne[t],(1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])
  	kb.add_clause([(1)*perceivedOne[t],(1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])
  	kb.add_clause([(-1)*perceivedOne[t],(1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])
  	kb.add_clause([(-1)*perceivedOne[t],(1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])
  	kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])
  	kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])
  	kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])

  if(t[0]==1):
    kb.add_clause([(1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])
    kb.add_clause([(1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])
    kb.add_clause([(1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])

    kb.add_clause([(-1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])
    kb.add_clause([(-1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])
    kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])
    kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)]])
    kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)]])

  if(t[1]==4):
    kb.add_clause([(1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]-1)]])
    kb.add_clause([(1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]-1)]])
    kb.add_clause([(1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]-1)]])

    kb.add_clause([(-1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]-1)]])
    kb.add_clause([(-1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]-1)]])
    kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]-1)]])
    kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]-1)]])
    kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]-1)]])

  if(t[1]==1):
    kb.add_clause([(1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)]])
    kb.add_clause([(1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)]])
    kb.add_clause([(1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)]])

    kb.add_clause([(-1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)]])
    kb.add_clause([(-1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)]])
    kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)]])
    kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(1)*hasMine[(t[0],t[1]+1)]])
    kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0]-1,t[1])],(-1)*hasMine[(t[0],t[1]+1)]])

#almost done 
#i'm guessing is fine

def move_four_direction(t,agent,possible_ans,s):
	if(canMoveUp[t]>0 and s!='Up' and visited[(t[0],t[1]+1)] < 0):
		agent.TakeAction('Up')
		return bfs(agent,possible_ans)

	if(canMoveRight[t]>0 and s!='Right' and visited[(t[0]+1,t[1])] < 0):
		agent.TakeAction('Right')
		return bfs(agent,possible_ans)

	if(canMoveLeft[t]>0 and s!='Left' and visited[(t[0]-1,t[1])] < 0):
		agent.TakeAction('Left')
		return bfs(agent,possible_ans)

	if(canMoveDown[t]>0 and s!='Down' and visited[(t[0],t[1]-1)] < 0):
		agent.TakeAction('Down')
		return bfs(agent,possible_ans)

	return []

#almost done 
#i'm guessing is fine






def if_zero(t,agent,possible_ans):

	if(canMoveUp[t]>0) :
		kb.add_clause([(-1)*abs(hasMine[(t[0],t[1]+1)])])
	if(canMoveRight[t]>0):
		kb.add_clause([(-1)*abs(hasMine[(t[0]+1,t[1])])])
	if(canMoveLeft[t]>0):
		kb.add_clause([(-1)*abs(hasMine[(t[0]-1,t[1])])])
	if(canMoveDown[t]>0):
		kb.add_clause([(-1)*abs(hasMine[(t[0],t[1]-1)])])
	if(canMoveUp[t]>0 and visited[(t[0],t[1]+1)] < 0):
		agent.TakeAction('Up')
		return bfs(agent,possible_ans)
	if(canMoveRight[t]>0 and visited[(t[0]+1,t[1])] < 0):
		agent.TakeAction('Right')
		return bfs(agent,possible_ans)


	if(canMoveLeft[t]>0 and visited[(t[0]-1,t[1])] < 0):
		agent.TakeAction('Left')
		return bfs(agent,possible_ans)

	if(canMoveDown[t]>0 and visited[(t[0],t[1]-1)] < 0):
		agent.TakeAction('Down')
		return bfs(agent,possible_ans)

	if(canMoveUp[t]>0) :
		agent.TakeAction('Up')
		# print('hi')
		return bfs(agent,possible_ans)


	if(canMoveRight[t]>0):
		agent.TakeAction('Right')
		return bfs(agent,possible_ans)

	
	if(canMoveLeft[t]>0):
		agent.TakeAction('Left')
		return bfs(agent,possible_ans)

	if(canMoveDown[t]>0):
		agent.TakeAction('Down')
		return bfs(agent,possible_ans)
    


	#dummy thing, should not be returned in any case
	#if is => there's something extremely wrong with the program
	return []
	
	
#almost done
#almost done
#i'm guessing is fine 
def one_two(t,agent,possible_ans):
	n=[[t[0],t[1]] for i in range(2)]
	action_x=''
	action_y=''
	if(t[0]==1 and t[1]==1):
		n[0][0]+=1
		action_x='Right'
		n[1][1]+=1
		action_y='Up'
	elif(t[0]==1 and t[1]==4):
		n[0][0]+=1
		action_x='Right'
		n[1][1]-=1
		action_y='Down'
	elif(t[0]==4 and t[1]==1):
		n[0][1]+=1
		action_x='Up'
		n[1][0]-=1
		action_y='Left'

	x=(n[0][0],n[0][1])
	y=(n[1][0],n[1][1])
	
	kb.add_clause([(-1)*perceivedOne[t],(1)*hasMine[x],(1)*hasMine[y]])
	kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[x],(-1)*hasMine[y]])
	kb.add_clause([(1)*perceivedOne[t],(-1)*hasMine[x],(1)*hasMine[y]])
	kb.add_clause([(1)*perceivedOne[t],(1)*hasMine[x],(-1)*hasMine[y]])

	x_kb=kb
	y_kb=kb

	# x_kb.add_clause([(-1)*hasMine[x]])
	# y_kb.add_clause([(-1)*hasMine[y]])

	if(not(x_kb.solve(assumptions=[(-1)*hasMine[x]]))):
		kb.add_clause([(1)*hasMine[x]])
		kb.add_clause([(-1)*hasMine[y]])
		agent.TakeAction(action_y)
		return bfs(agent,possible_ans)

	if(not(y_kb.solve(assumptions=[(-1)*hasMine[y]]))):
		kb.add_clause([(-1)*hasMine[x]])
		kb.add_clause([(1)*hasMine[y]])
		agent.TakeAction(action_x)
		return bfs(agent,possible_ans)

	if(x_kb.solve() and y_kb.solve()):
		ag1=copy.deepcopy(agent)
		h1=ag1.TakeAction(action_x)
		if(h1):
			kb.add_clause([(-1)*hasMine[x]])
			kb.add_clause([(1)*hasMine[y]])
			return bfs(agent,possible_ans)
		kb.add_clause([(1)*hasMine[x]])
		kb.add_clause([(-1)*hasMine[y]])
		return bfs(agent,possible_ans)

	#should not be returned in any case
	return []


#almost done
#i'm guessing is fine
def one_four(t,agent,possible_ans):
	#to be done
	kb.add_clause([(1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)],(1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)],(1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])

	kb.add_clause([(-1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(-1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(-1)*perceivedOne[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])

	kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)],(1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(1)*hasMine[(t[0]-1,t[1])]])

	kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(-1)*perceivedOne[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])




	#check which room is entailed to be unsafe
	x0=kb
	x1=kb
	x2=kb
	x3=kb

	# x0.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
	# x1.add_clause([(-1)*hasMine[(t[0],t[1]+1)]])
	# x2.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])
	# x3.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])


	if(not(x0.solve(assumptions=[(-1)*hasMine[(t[0]+1,t[1])]]))):
		kb.add_clause([(1)*hasMine[(t[0]+1,t[1])]])
		kb.add_clause([(-1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])
		return move_four_direction(t,agent,possible_ans,'Right')
	elif(not(x1.solve(assumptions=[(-1)*hasMine[(t[0],t[1]+1)]]))):
		kb.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
		kb.add_clause([(1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])
		return move_four_direction(t,agent,possible_ans,'Up')
	elif(not(x2.solve(assumptions=[(-1)*hasMine[(t[0],t[1]-1)]]))):
		kb.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
		kb.add_clause([(-1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])
		return move_four_direction(t,agent,possible_ans,'Down')
	elif(not(x3.solve(assumptions=[(-1)*hasMine[(t[0]-1,t[1])]]))):
		kb.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
		kb.add_clause([(-1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*hasMine[(t[0]-1,t[1])]])
		return move_four_direction(t,agent,possible_ans,'Left')

	#to be done
	#only way to resolve this is with 
	#the help of hit and try
	
	print("bjkl")
	l=len(possible_ans)
	t1=possible_ans[l-2]
	# print(t1)
	if(t1[0]==t[0]+1):
		agent.TakeAction('Right')
		return bfs(agent,possible_ans)
	if(t1[0]==t[0]-1):
		agent.TakeAction('Left')
		return bfs(agent,possible_ans)
	if(t1[1]==t[1]+1):
		agent.TakeAction('Up')
		return bfs(agent,possible_ans)
	if(t1[1]==t[1]-1):
		print("hello")
		agent.TakeAction('Down')
		return bfs(agent,possible_ans)

	return []
	return []


#almost done
#i'm guessing is fine

def one_three(t,agent,possible_ans):
	add_clauses_one_3(t)
	x0=kb
	x1=kb
	x2=kb
	if(t[0]==4):

		# x0.add_clause([(-1)*hasMine[(t[0],t[1]+1)]])
		# x1.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])
		# x2.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])
        
		if(not(x0.solve(assumptions=[(-1)*hasMine[(t[0],t[1]+1)]]))):
			kb.add_clause([(1)*hasMine[(t[0],t[1]-1)]])
			kb.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])
			kb.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])

			if(visited[(t[0]-1,t[1])] < 0):
				agent.TakeAction('Left')
				return bfs(agent,possible_ans)
			agent.TakeAction('Down')
			return bfs(agent,possible_ans)

		if(not(x1.solve(assumptions=[(-1)*hasMine[(t[0]-1,t[1])]]))):
			kb.add_clause([(-1)*hasMine[(t[0]+1,t[1]+1)]])
			kb.add_clause([(1)*hasMine[(t[0]-1,t[1])]])
			kb.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])

			if(visited[(t[0],t[1]+1)] < 0):
				agent.TakeAction('Up')
				return bfs(agent,possible_ans)
			agent.TakeAction('Down')
			return bfs(agent,possible_ans)

		if(not(x2.solve(assumptions=[(-1)*hasMine[(t[0],t[1]-1)]]))):
			kb.add_clause([(-1)*hasMine[(t[0]+1,t[1]+1)]])
			kb.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])
			kb.add_clause([(1)*hasMine[(t[0],t[1]-1)]])

			if(visited[(t[0],t[1]+1)] < 0):
				agent.TakeAction('Up')
				return bfs(agent,possible_ans)
			agent.TakeAction('Left')
			return bfs(agent,possible_ans)

	if(t[0]==1):
		# x0.add_clause([(-1)*hasMine[(t[0],t[1]+1)]])
		# x1.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
		# x2.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])
		print('Hi')
		if(not(x0.solve(assumptions=[(-1)*hasMine[(t[0],t[1]+1)]]))):
			print("sdrtyuio")
			kb.add_clause([(1)*hasMine[(t[0],t[1]+1)]])
			kb.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
			kb.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])

			if(visited[(t[0]+1,t[1])] < 0):
				agent.TakeAction('Right')
				return bfs(agent,possible_ans)
			agent.TakeAction('Down')
			return bfs(agent,possible_ans)

		if(not(x1.solve(assumptions=[(-1)*hasMine[(t[0]+1,t[1])]]))):
			print("sdrtyuio133333333333")
			kb.add_clause([(-1)*hasMine[(t[0],t[1]+1)]])
			kb.add_clause([(1)*hasMine[(t[0]+1,t[1])]])
			kb.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])

			if(visited[(t[0],t[1]+1)] < 0):
				agent.TakeAction('Up')
				return bfs(agent,possible_ans)
			agent.TakeAction('Down')
			return bfs(agent,possible_ans)

		if(not(x2.solve(assumptions=[(-1)*hasMine[(t[0],t[1]-1)]]))):
			print("sdrtyuio33333333333333333333")
			kb.add_clause([(-1)*hasMine[(t[0],t[1]+1)]])
			kb.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
			kb.add_clause([(1)*hasMine[(t[0],t[1]-1)]])

			if(visited[(t[0],t[1]+1)] < 0):
				agent.TakeAction('Up')
				return bfs(agent,possible_ans)
			agent.TakeAction('Right')
			return bfs(agent,possible_ans)

	if(t[1]==1):
		# x0.add_clause([(-1)*hasMine[(t[0],t[1]+1)]])
		# x1.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
		# x2.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])

		if(not(x0.solve(assumptions=[(-1)*hasMine[(t[0],t[1]+1)]]))):
			kb.add_clause([(1)*hasMine[(t[0],t[1]+1)]])
			kb.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])
			kb.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])

			if(visited[(t[0]+1,t[1])] < 0):
				agent.TakeAction('Right')
				return bfs(agent,possible_ans)
			agent.TakeAction('Left')
			return bfs(agent,possible_ans)

		if(not(x1.solve(assumptions=[(-1)*hasMine[(t[0]+1,t[1])]]))):
			kb.add_clause([(-1)*hasMine[(t[0],t[1]+1)]])
			kb.add_clause([(1)*hasMine[(t[0]+1,t[1])]])
			kb.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])

			if(visited[(t[0],t[1]+1)] < 0):
				agent.TakeAction('Up')
				return bfs(agent,possible_ans)
			agent.TakeAction('Left')
			return bfs(agent,possible_ans)

		if(not(x2.solve(assumptions=[(-1)*hasMine[(t[0]-1,t[1])]]))):
			kb.add_clause([(-1)*hasMine[(t[0],t[1]+1)]])
			kb.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
			kb.add_clause([(1)*hasMine[(t[0]-1,t[1])]])

			if(visited[(t[0]+1,t[1])] < 0):
				agent.TakeAction('Right')
				return bfs(agent,possible_ans)
			agent.TakeAction('Up')
			return bfs(agent,possible_ans)

	if(t[1]==4):
		# x0.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])
		# x1.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
		# x2.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])

		if(not(x0.solve(assumptions=[(-1)*hasMine[(t[0],t[1]-1)]]))):
			kb.add_clause([(1)*hasMine[(t[0],t[1]-1)]])
			kb.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
			kb.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])

			if(visited[(t[0]+1,t[1])] < 0):
				agent.TakeAction('Up')
				return bfs(agent,possible_ans)

			agent.TakeAction('Left')
			return bfs(agent,possible_ans)

		if(not(x1.solve(assumptions=[(-1)*hasMine[(t[0]+1,t[1])]]))):
			kb.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])
			kb.add_clause([(1)*hasMine[(t[0]+1,t[1])]])
			kb.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])

			if(visited[(t[0]-1,t[1])] < 0):
				agent.TakeAction('Left')
				return bfs(agent,possible_ans)

			agent.TakeAction('Down')
			return bfs(possible_ans)

		if(not(x2.solve(assumptions=[(-1)*hasMine[(t[0]-1,t[1])]]))):
			kb.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])
			kb.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
			kb.add_clause([(1)*hasMine[(t[0]-1,t[1])]])

			if(visited[(t[0]+1,t[1])] < 0):
				agent.TakeAction('Right')
				return bfs(agent,possible_ans)

			agent.TakeAction('Left')
			return bfs(agent,possible_ans)

	print("bjkl")
	l=len(possible_ans)
	t1=possible_ans[l-2]
	# print(t1)
	if(t1[0]==t[0]+1):
		agent.TakeAction('Right')
		return bfs(agent,possible_ans)
	if(t1[0]==t[0]-1):
		agent.TakeAction('Left')
		return bfs(agent,possible_ans)
	if(t1[1]==t[1]+1):
		agent.TakeAction('Up')
		return bfs(agent,possible_ans)
	if(t1[1]==t[1]-1):
		print("hello")
		agent.TakeAction('Down')
		return bfs(agent,possible_ans)

	return []

#almost done
#i'm guessing is fine

def more_four(t,agent,possible_ans):
	
	#add clauses
	kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])

	kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])

	kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)],(1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])

	#tbd
	kb.add_clause([(-1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(-1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(-1)*perceivedMore[t],(1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(-1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(-1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(-1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(-1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)],(1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(-1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(-1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(1)*hasMine[(t[0]-1,t[1])]])
	kb.add_clause([(-1)*perceivedMore[t],(-1)*hasMine[(t[0]+1,t[1])],(-1)*hasMine[(t[0],t[1]+1)],(-1)*hasMine[(t[0],t[1]-1)],(-1)*hasMine[(t[0]-1,t[1])]])

	x0=kb
	x1=kb
	x2=kb
	x3=kb
	h=[True for i in range(4)]
	h[0]=x0.solve(assumptions=[(-1)*hasMine[(t[0]+1,t[1])]])
	h[1]=x1.solve(assumptions=[(-1)*hasMine[(t[0],t[1]+1)]])
	h[2]=x2.solve(assumptions=[(-1)*hasMine[(t[0],t[1]-1)]])
	h[3]=x3.solve(assumptions=[(-1)*hasMine[(t[0]-1,t[1])]])
	# print()


    

	#x0->Right, x1-> Up, x2-> Down, x3-> Left
	if(not(h[0]) and not(h[1]) and not(h[2]) and not(h[3])):
		return []

	
	if(not(h[0]) and not(h[1]) and not(h[2])):
		kb.add_clause([(1)*hasMine[(t[0]+1,t[1])]])
		kb.add_clause([(1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])

		agent.TakeAction('Left')
		return bfs(agent,possible_ans)
	if(not(h[0]) and not(h[1]) and not(h[3])):
		kb.add_clause([(1)*hasMine[(t[0]+1,t[1])]])
		kb.add_clause([(1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*hasMine[(t[0]-1,t[1])]])

		agent.TakeAction('Down')
		return bfs(agent,possible_ans)
	if(not(h[0]) and not(h[2]) and not(h[3])):
		kb.add_clause([(1)*hasMine[(t[0]+1,t[1])]])
		kb.add_clause([(-1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*hasMine[(t[0]-1,t[1])]])

		agent.TakeAction('Up')
		return bfs(agent,possible_ans)
	if(not(h[3]) and not(h[1]) and not(h[2])):
		kb.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
		kb.add_clause([(1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*hasMine[(t[0]-1,t[1])]])

		agent.TakeAction('Right')
		return bfs(agent,possible_ans)

	if(not(h[0]) and not(h[1])):
		#add the required clauses
		kb.add_clause([(1)*hasMine[(t[0]+1,t[1])]])
		kb.add_clause([(1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])

		if(visited[(t[0]-1,t[1])] < 0):
			agent.TakeAction('Left')
			return bfs(agent,possible_ans)
		agent.TakeAction('Down')
		return bfs(agent,possible_ans)

	if(not(h[0]) and not(h[2])):
		#add the required clauses
		kb.add_clause([(1)*hasMine[(t[0]+1,t[1])]])
		kb.add_clause([(-1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])

		if(visited[(t[0],t[1]+1)] < 0):
			agent.TakeAction('Up')
			return bfs(agent,possible_ans)
		agent.TakeAction('Left')
		return bfs(agent,possible_ans)

	if(not(h[0]) and not(h[3])):
		#add the required clauses
		kb.add_clause([(1)*hasMine[(t[0]+1,t[1])]])
		kb.add_clause([(-1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*hasMine[(t[0]-1,t[1])]])

		if(visited[(t[0],t[1]+1)] < 0):
			agent.TakeAction('Up')
			return bfs(agent,possible_ans)
		agent.TakeAction('Down')
		return bfs(agent,possible_ans)


	if(not(h[1]) and not(h[2])):
		#add the required clauses
		kb.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
		kb.add_clause([(1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(-1)*hasMine[(t[0]-1,t[1])]])

		if(visited[(t[0]+1,t[1])] < 0):
			agent.TakeAction('Right')
			return bfs(agent,possible_ans)
		agent.TakeAction('Left')
		return bfs(agent,possible_ans)
		
	if(not(h[1]) and not(h[3])):
		#add the required clauses
		kb.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
		kb.add_clause([(1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(-1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*hasMine[(t[0]-1,t[1])]])

		if(visited[(t[0]+1,t[1])] < 0):
			agent.TakeAction('Right')
			return bfs(agent,possible_ans)

		agent.TakeAction('Down')
		return bfs(agent,possible_ans)

	if(not(h[2]) and not(h[3])):
		#add the required clauses
		kb.add_clause([(-1)*hasMine[(t[0]+1,t[1])]])
		kb.add_clause([(-1)*hasMine[(t[0],t[1]+1)]])
		kb.add_clause([(1)*hasMine[(t[0],t[1]-1)]])
		kb.add_clause([(1)*hasMine[(t[0]-1,t[1])]])

		if(visited[(t[0]+1,t[1])] < 0):
			agent.TakeAction('Right')
			return bfs(agent,possible_ans)
		agent.TakeAction('Up')
		return bfs(agent,possible_ans)

	print("bjkl")
	print("hi3,2")
	l=len(possible_ans)
	t1=possible_ans[l-2]
	# print(t1)
	if(t1[0]==t[0]+1):
		agent.TakeAction('Right')
		return bfs(agent,possible_ans)
	if(t1[0]==t[0]-1):
		agent.TakeAction('Left')
		return bfs(agent,possible_ans)
	if(t1[1]==t[1]+1):
		agent.TakeAction('Up')
		return bfs(agent,possible_ans)
	if(t1[1]==t[1]-1):
		print("hello")
		agent.TakeAction('Down')
		return bfs(agent,possible_ans)

	return []

	



	
	
	
	



#almost done
def more_three(t,agent,possible_ans):
	#add the clauses
	# print("addefdcns")	
	add_clauses_more_3(t)
	# print("Hiil;]")
	x0=kb
	#check for 3 mines
	# h0=False
	if(t[0]==4):
		h0=x0.solve(assumptions=[(-1)*abs(hasMine[(t[0],t[1]-1)])])
		h1=x0.solve(assumptions=[(-1)*abs(hasMine[(t[0],t[1]+1)])])
		h2=x0.solve(assumptions=[(-1)*abs(hasMine[(t[0]-1,t[1])])])
		# h3=x0.solve(assumptions=[abs(hasMine[(t[0]-1,t[1])])])
		
		if(not(h0) and not(h1) and not(h2)):
			kb.add_clause([hasMine[(t[0],t[1]-1)]])
			kb.add_clause([hasMine[(t[0]-1,t[1])]])
			kb.add_clause([hasMine[(t[0],t[1]+1)]])
			# kb.add_clause([hasMine[(t[0]+1,t[1])]])
			return []
	if(t[1]==4):
		h0=x0.solve(assumptions=[(-1)*abs(hasMine[(t[0]+1,t[1])])])
		h1=x0.solve(assumptions=[(-1)*abs(hasMine[(t[0],t[1]+1)])])
		h2=x0.solve(assumptions=[(-1)*abs(hasMine[(t[0]-1,t[1])])])
		# h3=x0.solve(assumptions=[abs(hasMine[(t[0]-1,t[1])])])
		
		if(not(h0) and not(h1) and not(h2)):
			kb.add_clause([hasMine[(t[0],t[1]-1)]])
			kb.add_clause([hasMine[(t[0]-1,t[1])]])
			# kb.add_clause([hasMine[(t[0],t[1]+1)]])
			kb.add_clause([hasMine[(t[0]+1,t[1])]])
			return []
	if(t[1]==1):
		# print("hjk")
		h0=x0.solve(assumptions=[(-1)*abs(hasMine[(t[0]+1,t[1])])])
		h1=x0.solve(assumptions=[(-1)*abs(hasMine[(t[0],t[1]+1)])])
		h2=x0.solve(assumptions=[(-1)*abs(hasMine[(t[0]-1,t[1])])])
		# h3=x0.solve(assumptions=[abs(hasMine[(t[0]-1,t[1])])])
		
		if(not(h0) and not(h1) and not(h2)):
			# print("fgyukl")
			kb.add_clause([hasMine[(t[0]-1,t[1])]])
			# kb.add_clause([hasMine[(t[0]-1,t[1])]])
			kb.add_clause([hasMine[(t[0],t[1]+1)]])
			kb.add_clause([hasMine[(t[0]+1,t[1])]])
			return []
	
	if(t[0]==1):
		h0=x0.solve(assumptions=[(-1)*abs(hasMine[(t[0]+1,t[1])])])
		h1=x0.solve(assumptions=[(-1)*abs(hasMine[(t[0],t[1]+1)])])
		h2=x0.solve(assumptions=[(-1)*abs(hasMine[(t[0],t[1]-1)])])
		# h3=x0.solve(assumptions=[abs(hasMine[(t[0]-1,t[1])])])
		
		if(not(h0) and not(h1) and not(h2)):
			# kb.add_clause([hasMine[(t[0],t[1]-1)]])
			kb.add_clause([hasMine[(t[0],t[1]-1)]])
			kb.add_clause([hasMine[(t[0],t[1]+1)]])
			kb.add_clause([hasMine[(t[0]+1,t[1])]])
			return []
	

	#you've to add clauses here
	print("its 2, so you've to backtrack again")
	l=len(possible_ans)
	t1=possible_ans[l-2]
	if(t1[0]==t[0]+1):
		if(canMoveLeft[t] > 0):
			kb.add_clause([abs(hasMine[(t[0]-1,t[1])])])
		if(canMoveDown[t] > 0):
			kb.add_clause([abs(hasMine[(t[0],t[1]-1)])])
		if(canMoveUp[t] > 0):
			kb.add_clause([abs(hasMine[(t[0],t[1]+1)])])
		agent.TakeAction('Right')
		return bfs(agent,possible_ans)
	if(t1[0]==t[0]-1):
		if(canMoveRight[t] > 0):
			kb.add_clause([abs(hasMine[(t[0]+1,t[1])])])
		if(canMoveDown[t] > 0):
			kb.add_clause([abs(hasMine[(t[0],t[1]-1)])])
		if(canMoveUp[t] > 0):
			kb.add_clause([abs(hasMine[(t[0],t[1]+1)])])
		agent.TakeAction('Left')
		return bfs(agent,possible_ans)
	if(t1[1]==t[1]+1):
		if(canMoveLeft[t] > 0):
			kb.add_clause([abs(hasMine[(t[0]-1,t[1])])])
		if(canMoveRight[t] > 0):
			kb.add_clause([abs(hasMine[(t[0]+1,t[1])])])
		if(canMoveDown[t] > 0):
			kb.add_clause([abs(hasMine[(t[0],t[1]-1)])])
		agent.TakeAction('Up')
		return bfs(agent,possible_ans)
	if(t1[1]==t[1]-1):
		if(canMoveLeft[t] > 0):
			kb.add_clause([abs(hasMine[(t[0]-1,t[1])])])
		if(canMoveRight[t] > 0):
			kb.add_clause([abs(hasMine[(t[0]+1,t[1])])])
		if(canMoveUp[t] > 0):
			kb.add_clause([abs(hasMine[(t[0],t[1]+1)])])
		agent.TakeAction('Down')
		return bfs(agent,possible_ans)

	return []
	

	





#free of translational disorder
def bfs(agent, possible_ans):
	# print('call')
	percept=agent.PerceiveCurrentLocation()
	tl=agent.FindCurrentLocation()
	t=(tl[0],tl[1])
    
	#base case
	if(t[0]==4 and t[1]==4):
		possible_ans.append(t)
		return possible_ans
	if((t[0]==4 and t[1]==3) or (t[0]==3 and t[0]==4)):
		possible_ans.append(t)
		possible_ans.append((4,4))
		return possible_ans


	if(visited[t] < 0):
		kb.add_clause([abs(visited[t])])
		visited[t]=abs(visited[t])

	possible_ans.append(t)

	kb.add_clause([(-1)*abs(hasMine[t])])
	if(percept == '=0'):
		print('percept 0')
		kb.add_clause([perceivedZero[t]])
		if_zero(t,agent,possible_ans)
    	

	elif(percept == '=1'):
		print('percept 1')
		kb.add_clause([perceivedOne[t]])
		if((t[0]==1 and t[1]==1) or (t[0]==1 and t[1]==4) or (t[0]==4 and t[1]==1)):
			print('debug_1_2')
			return one_two(t,agent,possible_ans)
			
		elif(canMoveLeft[t]>0 and canMoveRight[t]>0 and canMoveDown[t]>0 and canMoveUp[t]>0):
			print('debug_1_4')
			return one_four(t,agent,possible_ans)

		else:
			print('debug_1_3')
			return one_three(t,agent,possible_ans)

	else:
		print('percept more')
		kb.add_clause([perceivedMore[t]])


    	
		if((t[0]==1 and t[1]==1) or (t[0]==1 and t[1]==4) or (t[0]==4 and t[1]==1)):
			return []
		elif(canMoveLeft[t]>0 and canMoveRight[t]>0 and canMoveDown[t]>0 and canMoveUp[t]>0):
			print("cfghjk")
			return more_four(t,agent,possible_ans)

		else:
			print("cvbn")
			return more_three(t,agent,possible_ans)



        
    









		







def main():
	possible_ans=[]
	ag=Agent()
	kb.add_clause([(-1)*abs(hasMine[(1,1)])])
	kb.add_clause([(-1)*abs(hasMine[(4,4)])])
	print(kb.solve(assumptions=[(-1)*hasMine[(4,4)]]))
	print(kb.solve(assumptions=[(-1)*hasMine[(1,1)]]))
	bfs(ag,possible_ans)
	print(possible_ans)
	# print(type(visited))

   	
    


    

if __name__=='__main__':
    main()