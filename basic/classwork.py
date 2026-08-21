#water jug problem in bfs

from collections import deque
def bfs(j1,j2,target):
  visited= set()
  queue=deque([((0,0),[])])
  while queue:
    (a,b), path =queue.popleft()
    if a== target or b==target:
      for step in path + [(a,b)]: print(step)
      return 
    if(a,b) in visited: continue
    visited.add((a,b))
    next_states=[
          (j1,b), #fill jug1 to full
          (a,j2), #fill jug2 to full
          (0,b), #empty jug1
          (a,0),#empty jug2
          (min(a+b,j1),b-(min(a+b,j1)-a)), #pour jug --> jug 1, fill jug 1 as much as possible ,reduce jug
          (a-(min(a+b,j2)-b), min(a+b,j2)) #pour jug 1 -->jug2

      ]
    for s in next_states:
     if s not in visited:
              queue.append((s,path+ [(a,b)]))
    print("no solution posibble") #if the queue is exhausted without finding target, print "no solution possible"
bfs(4,3,2)
